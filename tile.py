import sqlite3

def read(sector):
    conn = sqlite3.connect('ThingDB.db')
    c = conn.cursor()
    return list(c.execute('''
        SELECT * FROM TILE WHERE Sector =?
    ''', [sector]))