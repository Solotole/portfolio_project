#!/usr/bin/python3
""" recommendations api module """
from models import storage
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models.book import Book
from models.user import User
from models.review import Review

@app_views.route('/recommendations/<id_user>', methods=['GET'], strict_slashes=False)
def recommend(id_user):
    """ route-method to recommend for books according to
        ratings, genre and author's name
    """
        # user data object
    user = storage.get(User, id_user)

    # Check if the user exists
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Retrieving user's reviews with a rating above 5
    user_reviews = storage.user_reviews(id_user)

    # Collect authors and genres from highly-rated books
    reviewed_authors = set()
    reviewed_genres = set()
    books_reviewed_ids = set()

    for review in user_reviews:
        reviewed_authors.add(review.book.author)
        reviewed_genres.add(review.book.genre)
        books_reviewed_ids.add(review.book.id)

    # Retrieve all books
    all_books = storage.all(Book).values()

    # Generate recommendations
    recommended_books = []
    for book in all_books:
        if book.id not in books_reviewed_ids and (book.author in reviewed_authors or book.genre in reviewed_genres):
            recommended_books.append(book)

    # Convert the recommended books to a serializable format
    recommended_books_serialized = [{'name': book.name, 'author': book.author, 'genre': book.genre} for book in recommended_books]

    return make_response(jsonify(recommended_books_serialized), 200)
