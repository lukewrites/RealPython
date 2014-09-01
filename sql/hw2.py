"""
Update the quantity on two of the records,
and then output all of the records from the table.
"""

import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # update two records in the db
    c.execute("UPDATE inventory SET Quantity = 18 WHERE Model = 'Fit'")
    c.execute("UPDATE inventory SET Quantity = 2 WHERE Model = 'Escort'")

    # output all records from the table
    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    print "\nCar Inventory:\n"

    for r in rows:
        print r[0], r[1]+':', r[2]