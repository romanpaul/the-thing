import random
import sqlite3

CHARACTER = {
    "Farrell": {
        "type": "Doug",
        "name": "Farrell",
        "captain power": "test"
        
    },
    "Brockman": {
        "type": "Doug",
        "name": "Farrell",
        "captain power": "test"
        
    },
    "Easter": {
        "type": "Doug",
        "name": "Farrell",
        "captain power": "test"
        
    }
}

def readList():
    conn = sqlite3.connect('ThingDB.db')
    c = conn.cursor()
    return list(c.execute('''
        SELECT * FROM CHARACTER ORDER BY Class ASC
    '''))