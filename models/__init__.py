#!/usr/bin/python3
""" models package """
from os import getenv
from models.engine.db_storage import DBStorage


if getenv('BRRS_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()