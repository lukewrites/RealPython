"""
Finally, output the car's make and model on one line, the quantity on another
line, and then the order_dates on subsequent lines below that.
"""

import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute()

    rows = c.fetchall()