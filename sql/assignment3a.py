import sqlite3
import random

# make a new db called newnum.db
with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE if exists random_numbers")
    c.execute("CREATE TABLE random_numbers(number INT)")

    # add 100 random ints range(0,100) to the db
    for i in range(100):
        c.execute("INSERT INTO random_numbers VALUES(?)",
                  (random.randint(0,100)))
        # wtf doesn't this work? getting:
        # ValueError: parameters are of unsupported type for line 13.