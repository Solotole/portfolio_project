#!/usr/bn/python3
""" app module """
from os import getenv
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from models.user import User

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown(exception):
    """
    teardown function
    """
    storage.close()

@app.errorhandler(404)
def err(error):
    """handle 404 error"""
    return make_response({"error": "Not found"}, 404)


if __name__ == "__main__":
    host = getenv('BRRS_MYSQL_HOST')
    port = getenv('BRRS_API_PORT')
    if not getenv('BRRS_MYSQL_HOST'):
        host = '0.0.0.0'
    if not getenv('BRRS_API_PORT'):
        port = 5000
    app.run(host=host, port=port, threaded=True)
