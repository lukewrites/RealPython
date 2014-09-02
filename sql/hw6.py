"""
Using the COUNT() function, calculate the total number of order for each make
and model.
"""

import sqlite3


with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    sql = {
            'Escape': "SELECT count(make) from orders WHERE make = 'Escape'",
            'Escort': "SELECT count(make) from orders WHERE make = 'Escort'",
            'F150': "SELECT count(make) from orders WHERE make = 'F150'",
            'CR-V': "SELECT count(make) from orders WHERE make = 'CR-V'",
            'Fit': "SELECT count(make) from orders WHERE make = 'Fit'"
    }

    for key, value in sql.iteritems(): # need to use iteritems()
        c.execute(value)
        result = c.fetchone()
        print key + ":", result[0]
