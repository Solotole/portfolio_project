#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
form models.user import User

app = Flask(__name__)

app.secret_key = 'brrs portfolio project'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'brrs_dev'
app.config['MYSQL_PASSWORD'] = 'Brrs_dev_pwd123!'
app.config['MYSQL_DB'] = ''

# Intialize MySQL
mysql = MySQL(app)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    """ method handling for login """
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        user = cursor.fetchone()
        # If account exists in accounts table in out database
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg='')