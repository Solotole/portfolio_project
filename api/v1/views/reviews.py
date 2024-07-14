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
    s = '%Y-%m-%dT%H:%M:%S.%f'
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
            "user_id": user_id[0:-1],
            "book_id": book_id
            }
    review = Review(**new_comment)
    storage.new(review)
    storage.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>/<id_user>', methods=['PUT'], strict_slashes=False)
def updating_review(review_id, id_user):
    """ updating a comment """
    instance = storage.get(Review, review_id)
    print(id_user)
    ignore = ['id', 'created_at', 'updated_at', 'book_id']
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
        if key not in ignore and instance.user_id == id_user:
            setattr(instance, key, value)
    new_instance = Review(instance)
    storage.save()
    return make_response(jsonify(new_instance.to_dict()), 200)


@app_views.route('/reviews/<review_id>/<id_user>', methods=['DELETE'], strict_slashes=False)
def delete_reviews(review_id, id_user):
    """ deleting a review """
    print(id_user)
    review = storage.get(Review, review_id)
    if review and review.user_id == id_user:
        storage.delete(review)
        storage.save()
    return make_response(jsonify({}), 200)
