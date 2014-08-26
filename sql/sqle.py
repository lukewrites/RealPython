# try/except

import sqlite3


# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

    # commit changes
    conn.commit()

except sqlite3.OperationalError:
    raise NameError

conn.close()
