# Fandor Challenge

## This is a challenge created for Fandor, where I made a mock film rating and filtering website.

## Contents
* [Technologies Used](#technologiesused)
* [Features](#feautures)
* [Main Page](#main)
* [Movie Search Page](#search)
* [How to locally run the Fandor Challenge](#run)

### <a name="technologiesused"></a>Technologies Used

* [SQLAlchemy](http://www.sqlalchemy.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Jinja](http://jinja.pocoo.org/)
* [Javascript](https://www.javascript.com/)
* [JQuery](https://jquery.com/)
* [JSON](http://www.json.org/)
* [AJAX](http://api.jquery.com/jquery.ajax/)
* [HTML/CSS](http://www.w3schools.com/html/html_css.asp)
* [Bootstrap](http://getbootstrap.com/)

### <a name="features"></a>Features

- [x] Movies filtered by popularity, year released, and all movies.
- [x] Movies can be searched by title, or description.
- [x] Movies are returned and divided by pagination.

#### <a name="main"></a>Main Movie Page
![fandor_challenge](https://cloud.githubusercontent.com/assets/11432315/24968447/1bdc576e-1f62-11e7-91b7-50c9a3ba63c3.gif)


Movies are organized by the following:
- Popularity
- Year released
- All films

Users can up vote or down vote each film with data retrieved in real time using AJAX and JSON.


#### <a name="search"></a>Movie Search Page
![fandor_challenge2](https://cloud.githubusercontent.com/assets/11432315/24941183/692066ec-1efd-11e7-9a48-21b3e8c9d3fc.gif)

Once typed in the search engine, movies are parsed by each word, and returned in real time using AJAX and JSON. The results are paginated using JQuery. 


#### <a name="run"></a>How to Run Fandor_Challenge locally

##### General Setup
* Set up and activate a python virtualenv, and install all dependencies:
    * `pip install -r requirements.txt`
  * Make sure you have PostgreSQL running. Create a new database in psql named fandor_challenge:
* `psql`
  * `createdb fandor_challenge`
 * Create the tables in your database:
    * `python -i model.py`
 * Then seed database
   * `python seed.py`
 * Start up the flask server:
    * `python server.py`
 * Go to localhost:5000 to see the web app
