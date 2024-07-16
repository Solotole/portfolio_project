#!/usr/bin/python3
""" Authentication module and book retrieval and recommendations route """
import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from uuid import uuid4
from models.book import Book
import MySQLdb.cursors
import hashlib
from models.user import User
from models import storage

app = Flask(__name__)

app.secret_key = 'brrs portfolio project'

# Enter your database connection details below
app.config['MYSQL_HOST'] = os.getenv('BRRS_MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('BRRS_MYSQL_USER', 'brrs_dev')
app.config['MYSQL_PASSWORD'] = os.getenv('BRRS_MYSQL_PWD', 'Brrs_dev_pwd123!')
app.config['MYSQL_DB'] = os.getenv('BRRS_MYSQL_DB', 'brrs_dev_db')

# Intialize MySQL
mysql = MySQL(app)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    """ method handling for login """
    # Output message if something goes wrong...
    msg = ''
    stringi = 'SELECT * FROM users WHERE email = %s AND password = %s'
    stringii = ' AND first_name = %s AND last_name = %s'
    stringiii = stringi + stringii
    if (request.method == 'POST' and 'email' in request.form and
        'last_name' in request.form and
        'first_name' in request.form and
        'password' in request.form):
        # Create variables for easy access
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        username = first_name + last_name
        hash = password + app.secret_key
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(stringiii, (email, password, first_name, last_name,))
        # Fetch one record and return result
        user = cursor.fetchone()
        # If account exists in accounts table in out database
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = user['id']
            session['first_name'] = user['first_name']
            session['last_name'] = user['last_name']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg='')


@app.route('/login/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('first_name', None)
    session.pop('last_name', None)
    # Redirecting to login page
    return redirect(url_for('login'))


@app.route('/login/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong
    msg = ''
    stringi = 'SELECT * FROM users email WHERE first_name = %s'
    # Checking if "names", "password" and "email" POST requests exist
    if (request.method == 'POST' and
        'last_name' in request.form and
        'first_name' in request.form and
        'password' in request.form and
        'email' in request.form):
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        # Checking if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(stringi, (email,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not first_name or not password or not email or not last_name:
            msg = 'Please fill out the form!'
        else:
            # Hash the password
            hash = password + app.secret_key
            # using sha1 instead of m256
            hash = hashlib.sha1(hash.encode())
            password = hash.hexdigest()
            user = {'email': email, 'first_name': first_name,
                    'last_name': last_name, 'password': password}
            instance = User(**user)
            instance.save()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/login/home')
def home():
    # Check if the user is logged in
    if 'loggedin' in session:
        # User is loggedin show them the home page
        first_name = session['first_name']
        last_name = session['last_name']
        username = first_name + ' ' + last_name
        return render_template('home.html', username=username)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/login/profile')
def profile():
    # Check if the user is logged in
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not logged in redirect to login page
    return redirect(url_for('login'))


@app.route('/brrs', strict_slashes=False)
def brrs():
    """ retriveing all books and rendering html """
    if 'loggedin' in session:
        books = {}
        cache_id = uuid4()
        books = storage.all(Book).values()
        # render html page with books data and user's id
        return render_template('0-index.html',
                                books=books,
                                cache_id=cache_id,
                                user_id=session['id'])
    return redirect(url_for('login'))


@app.route('/recommendations', strict_slashes=False)
def recommendations():
    """ recommendations according to user's reviews and rating """
    if 'loggedin' in session:
        cache_id = uuid4()
        # render html page with books data and user's id
        return render_template('2-index.html',
                                cache_id=cache_id,
                                user_id=session['id'])
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
