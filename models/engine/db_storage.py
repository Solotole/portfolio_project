#!/usr/bin/python3
""" Database storage mechanism """
from models.book import Book
from os import getenv
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.base_model import Base
from models.booksread import UserBook


classes = {'User': User, 'Review': Review, 'Book': Book, 'UserBook': UserBook}


class DBStorage:
    """ DBStorage class mechanism """
    __engine = None
    __storage = None

    def __init__(self):
        """ Class initialization magic method """
        string = 'mysql+mysqldb://{}:{}@{}/{}'
        user = getenv('BRRS_MYSQL_USER')
        pwd = getenv('BRRS_MYSQL_PWD')
        host = getenv('BRRS_MYSQL_HOST')
        db = getenv('BRRS_MYSQL_DB')
        env = getenv('BRRS_ENV')
        s = string.format(user, pwd, host, db)
        self.__engine = create_engine(s, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ querrying through a database """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload of data """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ closing the current session """
        self.__session.remove()

    def get(self, cls, id):
        """  method to retrieve one object """
        if not cls or not id:
            return None
        all_dicts = {}
        key = cls.__name__ + '.' + id
        all_dicts = self.all(cls)
        for keys in all_dicts.keys():
            if keys == key:
                return all_dicts[keys]
        return None

    def user_reviews(self, id_user):
        """ retrieving user's reviews with rating above 5 """
        only_user_reviews = []
        reviews = self.all(Review).values()
        for review in reviews:
            if review.user_id == id_user and review.rating >= 5:
                only_user_reviews.append(review)
        return only_user_reviews

    def get_read_books(self, user_id):
        """ Retrieve all books a user has read """
        read_books = []
        all_user_books = self.all(UserBook)
        print(all_user_books)
        all_books = self.all(Book).values()
        for user_book in all_user_books.values():
            for book in all_books:
                if user_book.user_id == user_id and book.id == user_book.book_id:
                    read_books.append(book)
        return read_books

