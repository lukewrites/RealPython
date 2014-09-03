import sqlite3


with sqlite3.connect("blog.db") as connection:
    # create a cursor
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE posts
              (title TEXT, post TEXT)
              """)

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")'),
    c.execute('INSERT INTO posts values("Well", "I\'m well.")'),
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")'),
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
