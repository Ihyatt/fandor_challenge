import unittest
from unittest import TestCase
from model import Movie, Ratings,connect_to_db, db
from server import app


class FandorChallenge(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()
		app.config['TESTING'] = True
		app.config['SECRET_KEY'] = 'key'
		# Connect to the database
		connect_to_db(app)

	def test_homepage(self):
		result = self.client.get("/")
		self.assertEqual(result.status_code, 200)

	def test_mainpage(self):
		result = self.client.get("/")

		self.assertIn("Popular", result.data)
		self.assertNotIn("Cool", result.data)

	def test_searchpage(self):
		result = self.client.get("/search")
		self.assertIn("Fandor", result.data)
		self.assertNotIn("Cool", result.data)

	def test_add_vote(self):
		result = self.client.post("/add-vote.json",
								data={"voted_item":"up",
								"movie_id": "3"}, 
								follow_redirects=True)

	def test_searchmovies(self):
		result = self.client.post('/movies_search.json', data={"search_item":"of course"}, 
								follow_redirects=True)


class TestFandorDatabase(unittest.TestCase):
	def setUp(self):
		"""Stuff to do before every test."""

		# Get the Flask test client
		self.client = app.test_client()

		# Show Flask errors that happen during tests
		app.config['TESTING'] = True

		# Connect to test database
		connect_to_db(app)


	def tearDown(self):
		"""Do at end of every test."""

		db.session.close()
		db.drop_all()





	




if __name__ == "__main__":
	unittest.main()