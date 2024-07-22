#!/usr/bin/python3
""" books api handler module """
from models import storage
from flask import jsonify
from api.v1.views import app_views
from models.book import Book
from models.review import Review


@app_views.route('/books', methods=['GET'], strict_slashes=False)
def retrieve_books():
    """ retrieving all books in database """
    all_books = storage.all(Book)
    all_list = []
    for key, value in all_books.items():
        all_list.append(value.to_dict())
    return jsonify(all_list)

@app_views.route('/books/<book_id>', methods=['GET'], strict_slashes=False)
def book_id_retrieval(book_id):
    """ retrieve a book based on reviews's id """
    all_reviews = storage.all(Review)
    all_book = []
    for key, value in all_reviews.items():
        if value.book_id == book_id:
            all_book.append(value.to_dict())
    return jsonify(all_book)

@app_views.route('/books/genre/<term>', methods=['GET'], strict_slashes=False)
def genre_book_search(term):
    """ searching and returning book acoording to passed genre identity """
    all_books = storage.all(Book)
    book = []
    if all_books:
        for key, value in all_books.items():
            if value.genre == str(term):
                book.append(value.to_dict())
    return jsonify(book)

@app_views.route('/books/author/<term>', methods=['GET'], strict_slashes=False)
def author_book_search(term):
    """ searching for books according to author name """
    all_books = storage.all(Book)
    book = []
    if all_books:
        for key, value in all_books.items():
            if value.author == str(term):
                book.append(value.to_dict())
    return jsonify(book)

@app_views.route('/books/name/<term>', methods=['GET'], strict_slashes=False)
def name_book_search(term):
    """ searching for books according to book name """
    all_books = storage.all(Book)
    book = []
    if all_books:
        for key, value in all_books.items():
            if value.name == str(term):
                book.append(value.to_dict())
    return jsonify(book)
