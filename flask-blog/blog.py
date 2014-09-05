from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3
from functools import wraps

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)


# function used for connection to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first, fool.')
            return redirect(url_for('login'))
    return wrap


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                        request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)


@app.route('/main')
@login_required  # this is a call to the login_required() function above.
                 # so when someone tries to go to '/main', login_required()
                 # automatically gets called.
                 # By default, routes respond to GET requests.
def main():
    g.db = connect_db()  # connect to db
    cur = g.db.execute('select * from posts')  # fetch data from posts table
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    # a list comp to pull the title and the text of the post for each post in db
    g.db.close()  # close the connection
    return render_template('main.html', posts=posts)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']  # get the title from the form
    post = request.form['post']    # get the post txt from the form
    if not title or not post:      # if they didn't fill out one or both box...
        flash("You have to have both a title and a post. Try again.")
        return redirect(url_for('main'))
    else:  # otherwise, go ahead and get this into the db.
        g.db = connect_db()
        g.db.execute('INSERT INTO posts (title, post) values(?, ?)',
                     [request.form['title'], request.form['post']])
                     # note the use of parametrized statements. nice.
        g.db.commit()
        g.db.close()
        flash('New entry successfully added!')
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
