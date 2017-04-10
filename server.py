"""Fandor Challenge"""

import os
from jinja2 import StrictUndefined
import psycopg2

from model import Movie, Ratings, connect_to_db, db

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def main_page():
    """Main page where movies will be displayed"""
    movies = Movie.query.all()

    return render_template("home.html", movies=movies)

@app.route("/add-vote.json", methods=['POST']) 
def rate_movie():
	"""Rate movie"""

	voted_item = request.form.get("voted_item")
	movie_id = request.form.get("movie_id")

	movie = Movie.query.get(int(movie_id))
	vote_added = None
	if voted_item == "up":
		vote_added = Ratings(movie_id=int(movie_id), up_vote=True, down_vote=False)
	else:
		vote_added = Ratings(movie_id=int(movie_id), up_vote=False, down_vote=True)

	db.session.add(vote_added)
	db.session.commit()

	result = {'vote': movie.rating_count(), "movie_id": movie_id}
	return jsonify(result)


@app.route('/search')
def search_page():
	"""Search page where user queries for specific movies"""

	return render_template("search.html")

@app.route('/movies_search',methods=['GET'])
def return_search():
	query = {}
	search_list = []
	search = request.args.get("search_item")
	splitted_search = search.split(" ")

	for word in splitted_search:
		search_match = Movie.query.filter(Movie.title.like('%' + word + '%') ).all() 
		search_list.extend(search_match)
	
	for match in search_list:
		query[match.movie_id] = [match.title, match.description, match.year]

	print query

	return jsonify(query)






if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run()