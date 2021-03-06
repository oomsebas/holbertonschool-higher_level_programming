#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv


def get_all_states(username, password, dbname):
    """function that returns all the states from a database
    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname))
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
                states ON cities.state_id = states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    get_all_states(argv[1], argv[2], argv[3])
