"""Utility file to seed fandor_challenge database from  data in seed_data/"""


from sqlalchemy import func
import json
from model import Ratings, Movie, connect_to_db, db
from server import app
from pprint import pprint

def seed_movies():
	"""loads movies into database"""
	with open('films.json') as data_file:    
	    data = json.load(data_file)
	for item in data:
		for group in data[item]:
			title = group["title"]
			description = group["description"]
			url_slug = group["url_slug"]
			year = group["year"]
			related_film_ids = str(group["related_film_ids"])[1:-1]




			movie = Movie(title=title, description=description, url_slug=url_slug, year=year, related_film_ids=related_film_ids)

			db.session.add(movie)
	db.session.commit()





if __name__ == "__main__":
    connect_to_db(app)
    print seed_movies()