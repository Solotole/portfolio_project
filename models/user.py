#!/usr/bin/python3
""" User module representation """
from flask_login import UserMixin
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base, UserMixin):
    """ User class-table mapping representation """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    reviews = relationship('Review', back_populates='user',
                           cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ initialization method of class User"""
        super().__init__(*args, **kwargs)

    def get_id(self):
        return str(self.id)