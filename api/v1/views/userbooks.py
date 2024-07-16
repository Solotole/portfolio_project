#!/usr/bin/python3
""" user books read module
    this API module handles the books the user has read
"""
from models import storage
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models.booksread import UserBook


@app_views.route('/users/<user_id>/read', methods=['POST'], strict_slashes=False)
def mark_as_read(user_id):
    """ Mark a book as read """
    book_id = request.json.get('book_id')
    if not book_id:
        return abort(400, description="book_id is required")
    dictionary = {'user_id': user_id, 'book_id': book_id}
    read_entry = UserBook(**dictionary)
    storage.new(read_entry)
    storage.save()
    return make_response(jsonify(read_entry.to_dict()), 201)


@app_views.route('/users/<user_id>/read', methods=['GET'], strict_slashes=False)
def get_read_books(user_id):
    """ Get books a user has read """
    read_books = storage.get_read_books(user_id)
    return jsonify([book.to_dict() for book in read_books])
