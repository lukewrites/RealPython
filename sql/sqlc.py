# executemany() method

import sqlite3


# use with to create a connection to new.db. name this 'connection'
with sqlite3.connect("new.db") as connection:
    # make a cursor
    c = connection.cursor()

    # insert multiple records using a tuple
    cities = [
        ('Boston', 'MA', 6000000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000)
    ]

    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
