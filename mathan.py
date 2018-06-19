
import sqlite3
import json

DB = "./mathankumar.db"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect("mathankumar.db")
connection.row_factory = dict_factory

cursor = connection.cursor()

cursor.execute('''select * from mathan''')

cursor.fetchall()
