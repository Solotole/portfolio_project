#!/usr/bin/python3
""" Books module representation """
from sqlalchemy import String, Column
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Book(BaseModel, Base):
    """ Books class-table mapping """
    __tablename__ = 'books'  # name of table in database

    name = Column(String(60), nullable=False)
    genre = Column(String(60), nullable=False)
    author = Column(String(60), nullable=False)
    download_link = Column(String(255), nullable=True)  # book downloading link

    reviews = relationship('Review', back_populates='book',
                           cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ Book class initialization special method """
        # calling BaseModel __init__ magic method
        super().__init__(*args, **kwargs)
