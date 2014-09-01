# coding=utf-8
""" Using the “inventory” table from the previous homework assignment,
add(INSERT) 5records (rows of data) to the table. Make sure 3 of the vehicles are
Fords while the other 2 are Hondas. Use any model and quantity for each.
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    new_inventory = [
        ('Ford', 'Escort', 23),
        ('Honda', 'Fit', 15),
        ('Ford', 'Escape', 2),
        ('Honda', 'CR-V', 8),
        ('Ford', 'F150', 1)
    ]

    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", new_inventory)
