#!/usr/bin/python3
""" Review module representation """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Reviews class-table mapping """
    __tablename__ = "reviews"

    text = Column(String(128), nullable=False)
    rating = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(60), ForeignKey('books.id'), nullable=False)

    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='reviews')

    def __init__(self, *args, **kwargs):
        """ initialization method of class """
        super().__init__(*args, **kwargs)
