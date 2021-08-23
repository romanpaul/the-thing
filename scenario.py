import random
import sqlite3

# Returns a single random card
def read():
    #return random.choice(list(SCENARIO.values()))
    conn = sqlite3.connect('ThingDB.db')
    c = conn.cursor()
    return list(c.execute('''
        SELECT * FROM SCENARIO ORDER BY RANDOM() LIMIT 1
    '''))
