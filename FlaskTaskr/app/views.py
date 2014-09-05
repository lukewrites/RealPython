from flask import Flask, flash, redirect, render_template, request, \
    session, url_for, g
from functools import wraps
import sqlite3

app = Flask(__name__)
app.config.from_object('config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_requred(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first')
            return redirect(url_for('login'))
        return wrap
asdf

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You are logged out. Buh-bye!')
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            return redirect(url_for('tasks'))
    return render_template('login.html', error=error)