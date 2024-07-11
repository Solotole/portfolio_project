#!/usr/bin/python3
""" Base class of the project """
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
import models


Base = declarative_base()


class BaseModel:
    """ Base class representation """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ class initialization """
        s = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get('created_at', None):
                self.created_at = datetime.strptime(kwargs['created_at'], s)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('id', None) is None:
                self.id = str(uuid4())
            if kwargs.get('updated_at', None):
                self.updated_at = datetime.utcnow()
        elif not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """ str magic method representation """
        class_name = self.__class__.__name__
        identity = self.id
        return '[{}]--[{}]  {}'.format(class_name, identity, self.__dict__)

    def save(self):
        """ saves and updates updated_at attribute to current time """
        self.udated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns altered dictionary of an instance """
        s = '%Y-%m-%dT%H:%M:%S.%f'
        dictionary = self.__dict__.copy()
        if '__class__' not in dictionary:
            dictionary['__class__'] = self.__class__.__name__
        if 'created_at' in dictionary:
            dictionary['created_at'] = dictionary['created_at'].strftime(s)
        if 'updated_at' in dictionary:
            dictionary['updated_at'] = dictionary['updated_at'].strftime(s)
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ deleting from storage database """
        models.storage.delete(self)
