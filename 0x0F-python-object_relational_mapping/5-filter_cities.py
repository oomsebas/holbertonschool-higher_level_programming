#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv


def get_all_states(username, password, dbname, stname):
    """function that returns all the states from a database
    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname))
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities RIGHT JOIN\
                states ON cities.state_id=states.id\
                WHERE states.name=%(state)s",
                {'state': stname})
    rows = cur.fetchall()
    if rows:
        for row in rows:
            if row is rows[-1]:
                print(row[0])
            else:
                print(row[0], end=", ")
    else:
        print()
    cur.close()
    db.close()

if __name__ == '__main__':
    get_all_states(argv[1], argv[2], argv[3], argv[4])
