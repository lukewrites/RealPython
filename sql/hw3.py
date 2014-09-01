"""
Finally, output only records that are for Ford vehicles.
"""

import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # get the Ford vehicles
    c.execute("SELECT * FROM inventory WHERE Make = 'Ford'")

    rows = c.fetchall()

    print "Ford Inventory:"

    for r in rows:
        print r[0], r[1], r[2]