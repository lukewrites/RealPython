"""
Finally, output the car's make and model on one line, the quantity on another
line, and then the order_dates on subsequent lines below that.
"""

import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT inventory.Make, inventory.Model,
                  inventory.Quantity, orders.order_date FROM inventory, orders
                  WHERE inventory.Model == orders.make
                  ORDER BY inventory.Make DESC""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print 'Quantity: ', r[2]
        print r[3], '\n'