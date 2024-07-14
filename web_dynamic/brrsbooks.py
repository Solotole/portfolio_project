#!/usr/bin/python3
""" serving books list """
from models import storage
from models.book import Book
from flask import Flask, render_template
from uuid import uuid4

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/brrs', strict_slashes=False)
def brrs():
    """ retriveing all books and rendering html """
    from auth import session
    books = {}
    cache_id = uuid4()
    books = storage.all(Book).values()
    return render_template('0-index.html',
                            books=books,
                            cache_id=cache_id,
                            user_id=session['id'])

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5002)
