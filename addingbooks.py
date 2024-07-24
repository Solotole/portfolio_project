#!/usr/bin/python3
""" Module responsinle for accessing books data from
    Project Gutenberg API, storing in MySQL database
    , and dowloading and storing in a directory
"""
import requests
import os
from models.engine.db_storage import DBStorage
from models.book import Book

storage = DBStorage()
storage.reload()


def add_book_to_db(name, author, genre, download_link):
    """ Adds a book to the database """
    new_book = Book(
        name=name,
        author=author,
        genre=genre,
        download_link=download_link
    )
    storage.new(new_book)
    storage.save()
    return new_book


def extract_genre(subjects):
    """ Extracts the last word after the last '-' in the genre string """
    if subjects:
        last_subject = subjects[2] if len(subjects) >= 3 else subjects[-1]
        parts = last_subject.split('--')
        if len(parts) > 1:
            genre = parts[-1].strip()
        else:
            genre = last_subject.strip()
    else:
        genre = 'Unknown Genre'
    return genre


def fetch_and_store_book():
    """ Fetches book metadata and stores it in the database """
    base_url = 'http://gutendex.com/books/'
    # Defining the parameters to limit the results to 10 books
    params = {'limit': 10}
    # Sending a GET request to the API
    response = requests.get(base_url, params=params)
    book_data = response.json()
    for books in book_data['results']:
        name = books.get('title', 'Unknown Title')
        author = books.get('authors', [{'name': 'Unknown Author'}])[0]['name']
        subjects = books.get('subjects', [])
        genre = extract_genre(subjects)
        download_formats = books.get('formats', {})
        download_link = download_formats.get('text/html; charset=utf-8')
        if download_link:
            dict_object = add_book_to_db(name, author, genre, download_link)
            download_book(books['id'], download_link, dict_object)


def download_book(book_id, download_link, dict_object):
    """ Downloads the book and saves it to a specified directory """
    response = requests.get(download_link)
    response.raise_for_status()  # Raise an error for bad status codes
    file_path = f"files/{dict_object.id}.html"

    # Ensuring the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {book_id} to {file_path}")
    return file_path


if __name__ == '__main__':
    fetch_and_store_book()
