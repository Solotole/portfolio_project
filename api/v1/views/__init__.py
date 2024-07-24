#!/usr/bin/python3
""" views iporting blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.books import *
from api.v1.views.reviews import *
from api.v1.views.recommendations import *
from api.v1.views.userbooks import *
from api.v1.views.messages import *
