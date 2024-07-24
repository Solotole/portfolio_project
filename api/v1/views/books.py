#!/usr/bin/python3
""" books api handler module """
from models import storage
from flask import jsonify, make_response, send_from_directory
from api.v1.views import app_views
from models.book import Book
from models.review import Review
import os


@app_views.route('/books', methods=['GET'], strict_slashes=False)
def retrieve_books():
    """ retrieving all books in database """
    all_books = storage.all(Book)
    all_list = []
    # looping over all books dictionaries
    for key, value in all_books.items():
        all_list.append(value.to_dict())
    return jsonify(all_list)


@app_views.route('/books/<book_id>', methods=['GET'], strict_slashes=False)
def book_id_retrieval(book_id):
    """ retrieve a book based on reviews's id """
    all_reviews = storage.all(Review)
    all_book = []
    # looping over all reviews dictionaries
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
        # looping over all books dictionaries
        for key, value in all_books.items():
            # compare if same as the genre user entered
            if value.genre == str(term):
                book.append(value.to_dict())
    return jsonify(book)


@app_views.route('/books/author/<term>', methods=['GET'], strict_slashes=False)
def author_book_search(term):
    """ searching for books according to author name """
    all_books = storage.all(Book)
    book = []
    if all_books:
        # looping over all books dictionaries
        for key, value in all_books.items():
            # compare if same as the author user entered
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
            # compare if same as the title user entered
            if value.name == str(term):
                book.append(value.to_dict())
    return jsonify(book)


@app_views.route('/books/download/<book_id>', methods=['GET'],
                 strict_slashes=False)
def download_file(book_id):
    # Defining the path to the directory where files are stored
    book = storage.get(Book, book_id)
    if not book:
        return make_response(jsonify({'error': 'Book not found'}), 404)
    directory = os.path.join(os.getcwd(), 'files')
    # Defining the filename with .html extension
    filename = f"{book_id}.html"
    # Checking if the file exists
    if not os.path.exists(os.path.join(directory, filename)):
        abort(404, description="File not found")
    return send_from_directory(directory, filename, as_attachment=True)
