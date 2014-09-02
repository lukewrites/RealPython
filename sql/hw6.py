"""
Using the COUNT() function, calculate the total number of order for each make
and model.
"""

import sqlite3


with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    sql = {
            "SELECT count(make) from orders WHERE make = 'Escape'",
            "SELECT count(make) from orders WHERE make = 'Escort'",
            "SELECT count(make) from orders WHERE make = 'F150'",
            "SELECT count(make) from orders WHERE make = 'CR-V'",
            "SELECT count(make) from orders WHERE make = 'Fit'",
    }
