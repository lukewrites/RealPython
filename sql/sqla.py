import sqlite3


#create a new database if it doesn't already exist.
conn = sqlite3.connect("cars.db")

# get a cursor object to execute SQL commands.
cursor = conn.cursor()

# create a table.
cursor.execute("""CREATE TABLE inventory
                  (Make TEXT, Model TEXT, Quantity INT)
                  """)

# close the connection.
conn.close()