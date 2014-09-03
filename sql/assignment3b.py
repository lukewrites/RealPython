import sqlite3


# user prompt: aggregation or exit
def welcome():
    task = raw_input("""Which of the following would you like to do?
                        1. Calculate average
                        2. Find minimum value
                        3. Find maximum value
                        4. Calculate the sum
                        5. Quit""")
    # basic setup: connect to the db
    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()
        while True:
            if task is not in range(5):
                welcome()

    # aggregations: AVG, MIN, MAX, SUM