# UPDATE and DELETE statements

import sqlite3


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # update data
    c.execute("UPDATE population SET population = 9000000 WHERE city='New YorkCity'")

    # delete data
    c.execute("DELETE FROM population where city = 'Boston'")


