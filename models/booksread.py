#!/usr/bin/pyhton3
""" module to represent table books read by the user """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class UserBook(BaseModel, Base): # multiple inheritance of the base class and Base
    """ Class-table to represent books read by the user """
    __tablename__ = 'userbooks'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(60), ForeignKey('books.id'), nullable=False)
    
    def __init__(self, *args, **kwargs):
        """ UserBook class initialization special method """
        super().__init__(*args, **kwargs) # parsing to Base class __init__ magic method
