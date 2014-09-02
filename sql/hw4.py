"""
Add another table to accompany your 'inventory' table called 'orders'.
This table should have the following fields: 'make', 'model', and
'order_date'. Add 15 records (3 for each car), each with a separate order
date (YYYY-MM-DD). Research how to do that.
"""

import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders
              (make TEXT, model TEXT, order_date TEXT)
              """)

    sales_data = [
        ('Fit', 'Sport', '2014-03-03'),
        ('Fit', 'Base', '2013-05-05'),
        ('Escape', 'Luxe', '2014-06-06'),
        ('Escort', 'Base', '2013-01-01'),
        ('CR-V', 'Base', '2014-05-05'),
        ('CR-V', 'Base', '2014-05-06'),
        ('CR-V', 'Sport', '2014-03-03'),
        ('Escape', 'Luxe', '2014-06-06'),
        ('Escort', 'Base', '2014-11-11'),
        ('F150', 'Base', '2014-02-02'),
        ('Escape', 'Sport', '2014-12-12'),
        ('F150', 'Diesel', '2014-02-05'),
        ('F150', 'Diesel', '2014-07-12'),
        ('F150', 'Diesel', '2014-06-12'),
        ('Escort', 'Base', '2014-11-10')
    ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", sales_data)