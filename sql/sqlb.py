import sqlite3

"""
refactor to use the 'with' keyword.
this will make it autosave upon completion, and you don't have to worry about
remembering to commit or closing the connection.
"""

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    c.execute("INSERT INTO population VALUES('San Francisco', 'SF', 800000)")

