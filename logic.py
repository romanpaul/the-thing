import sqlite3 as sql
import secrets

# generates a random string for API key
generated_key = None

def insertUser(userID, password):
	global generated_key 
	generated_key = secrets.token_urlsafe(10)
	conn = sql.connect("ThingDB.db")
	cur = conn.cursor() 
	cur.execute("INSERT INTO user (key,userID,password) VALUES (?,?,?)", (generated_key,userID,password))
	conn.commit()
	conn.close()
