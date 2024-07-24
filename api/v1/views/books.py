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

from flask import send_from_directory

@app_views.route('/books/download/<book_id>', methods=['GET'], strict_slashes=False)
def download_file(book_id):
    # Define the path to the directory where files are stored
    book = storage.get(Book, book_id)
    if not book:
        return make_response(jsonify({'error': 'Book not found'}), 404)
    directory = os.path.join(os.getcwd(), 'files')
    # Define the filename with .html extension
    filename = f"{book_id}.html"
    # Check if the file exists
    if not os.path.exists(os.path.join(directory, filename)):
        abort(404, description="File not found")
    return send_from_directory(directory, filename, as_attachment=True)

# @app_views.route('/books/download/<book_id>', methods=['GET'], strict_slashes=False)
# def download_book_file(book_id):
    # """ Serve the book file from the server """
    # file_path = f"/{book_id}.html"
    # Retrieve the book from the database using book_id
    # book = storage.get(Book, book_id)
    # if not book:
        # return make_response(jsonify({'error': 'Book not found'}), 404)
        
    # Set the file path and filename
    # directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../files')
    # filename = f"{book_id}.html"  # Ensure this matches the actual file format

    # Checking if file exists before attempting to send it
    # file_path = os.path.join(directory, filename)
    # if not os.path.exists(file_path):
        # print(f"File does not exist at path: {file_path}")
        # return jsonify({'error': 'File not found'}), 404

    # Serving the file for download
    # return send_from_directory(directory=directory,
                               # filename=filename,
                               # as_attachment=True,
                               # attachment_filename=f"{book.name}.html")
