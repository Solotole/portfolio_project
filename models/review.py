#!/usr/bin/python3
""" Review module representation """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base): # multiple inheritance
    """ Reviews class-table mapping """
    __tablename__ = "reviews"

    # review comment
    text = Column(String(128), nullable=False)
    # rating 0-10
    rating = Column(Integer, nullable=False)
    # user's unique id
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(60), ForeignKey('books.id'), nullable=False)

    # relation to users table reviews
    user = relationship('User', back_populates='reviews')
    # relation to books table reviews
    book = relationship('Book', back_populates='reviews')

    def __init__(self, *args, **kwargs):
        """ initialization method of class """
         # addressing superclass initialization magic method
        super().__init__(*args, **kwargs)
