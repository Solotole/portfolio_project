#!/usr/bin/python3
""" reviews api module """
from models import storage
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models.book import Book
from models.review import Review


@app_views.route('/reviews/<book_id>', methods=['GET'], strict_slashes=False)
def retrieving_book_reviews(book_id):
    """ retrieving all reviews to a book """
    all_reviews = storage.all(Review)
    list_reviews = []
    for key, value in all_reviews.items():
        if value.book_id == str(book_id):
            list_reviews.append(value.to_dict())
    return list_reviews


@app_views.route('/books/<user_id>/<book_id>/reviews', methods=['POST'], strict_slashes=False)
def posting_review(user_id, book_id):
    """ posting a new review comment to a book """
    new_comment = {}
    data = request.get_json()
    if not request.get_json():
        abort(400, description="request not json format")
    if 'text' not in request.get_json():
        abort(400, description="missing text")
    if 'rating' not in request.get_json():
        abort(400, description="missing rating")
    comment = data['text']
    rate = data['rating']
    new_comment = {
            "text": comment,
            "rating": rate,
            "user_id": user_id,
            "book_id": book_id
            }
    instance = Review(**new_comment)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def updating_review(review_id):
    """ updating a comment """
    instance = storage.get(Review, review_id)
    ignore = ['id', 'created_at', 'updated_at', 'user_id', 'book_id']
    data = request.get_json()
    if not request.get_json():
        abort(400, description="zero request data")
    if not instance:
        abort(400, description="object not existing")
    if 'text' not in data:
        abort(400, description="no text in request")
    if 'rating' not in data:
        abort(400, description="no rating argument in request")
    for key, value in data.items():
        if key not in ignore:
            setattr(instance, key, value)
    new_instance = Review(instance)
    storage.save()
    return make_response(jsonify(new_instance.to_dict()), 200)


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_reviews(review_id):
    """ deleting a review """
    review = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        storage.save()
    return make_response(jsonify({}), 200)