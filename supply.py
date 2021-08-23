import random
import sqlite3
import sqlalchemy
import pandas as pd
from flask.json import jsonify


engine = sqlalchemy.create_engine('sqlite:///ThingDB.db')
sql_data = pd.read_sql_table('SUPPLY', engine).to_json

# Returns five random cards to form a new hand
def read():
    #return random.sample(list(SUPPLY), 5)
    conn = sqlite3.connect('ThingDB.db')
    c = conn.cursor()
    return list(c.execute('''
        SELECT * FROM SUPPLY ORDER BY RANDOM() LIMIT 5
    '''))
    
# Returns a single random card
def readOne():
    #return random.choice(sql_data)
    #return sql_data.sample()
    conn = sqlite3.connect('ThingDB.db')
    c = conn.cursor()
    return list(c.execute('''
        SELECT * FROM SUPPLY ORDER BY RANDOM() LIMIT 1
    '''))