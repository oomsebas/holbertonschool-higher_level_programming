#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


def get_all_states(username, password, dbname, stname):
    """function that returns all the states from a database
    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname), charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s;",(stname,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    get_all_states(argv[1], argv[2], argv[3], argv[4])
