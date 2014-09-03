"""
Output car's make & model on one line, quantity on the next, and then the order
count on the next line.
"""

import sqlite3


with sqlite3.connect("cars.db") as connect:
    c = connect.cursor()
    # get make, model, and quantity
    c.execute("""SELECT * from inventory""")
    rows = c.fetchall()
    # print make & model on one line
    for row in rows:
        print row[0], row[1], '\n', row[2]
        # print quantity
        m = row[0]
        c.execute("SELECT count(order_date) FROM orders WHERE make=?", (m,))
        # this wasn't working because I didn't have the trailing comma
        # found the answer on SO:
        # http://stackoverflow.com/questions/11853167/parameter-unsupported-when-inserting-int-in-sqlite
        order_count = c.fetchone()[0]
        print order_count