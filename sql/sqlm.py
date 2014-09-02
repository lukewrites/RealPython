# sqlite functions

import sqlite3


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a ductionary of sql questies
    sql = {'average': 'SELECT avg(POPULATION) FROM population',
           'maximum': 'SELECT max(POPULATION) FROM population',
           'minimum': "SELECT min(POPULATION) FROM population",
           'sum': 'SELECT sum(POPULATION) FROM population',
           'count': 'SELECT count(POPULATION) FROM population'}

    for keys, values in sql.iteritems(): # iterates over k:v pairs in dict.
        # run sql
        c.execute(values)
        # fetchone() retrieves one record from the query
        result = c.fetchone()
        # output the results to screen
        print keys + ':', result[0]