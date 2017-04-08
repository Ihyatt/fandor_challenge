"""Models and database functions for Ratings project."""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os


# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)


db = SQLAlchemy()

##############################################################################
# Model definitions

class Movie(db.Model):
	__tablename__ = "movies"

	movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(100), nullable=True)
	description = db.Column(db.String(100), nullable=True)
	url_slug = db.Column(db.String(100),nullable=True)
	year = db.Column(db.Integer, nullable=True)
	related_film_ids = db.Column(db.String(100),nullable=True)

class Ratings(db.Model):
	__tablename__ = "ratings"

	rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), index=True)
	score = db.Column(db.Integer, nullable=True)

	movie = db.relationship("Movie", backref=db.backref("ratings", order_by=rating_id))




def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///fandor_challenge' 
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print "Connected to DB."
    db.create_all()


