import sqlite3
import pandas as pd

# Creates DB file if one with this name does not exist
conn = sqlite3.connect('ThingDB.db')
c = conn.cursor()

""" c.execute('''
            INSERT INTO CHARACTER
            VALUES ('Blair', 'Science', 'Reroll any one die'),
            ('Fuchs', 'Science', 'Reroll any one die'),
            ('Bennings', 'Science',	'Reroll any one die'),
            ('Norris', 'Science', 'Reroll any one die'),
            ('Clark', 'Maintanance', 'Add +1 to any one die'),
            ('Palmer', 'Maintanance', 'Add +1 to any one die'),
            ('Childs', 'Maintanance', 'Add +1 to any one die'),
            ('Copper', 'Operations', 'Reroll ALL dice'),
            ('Windows',	'Operations', 'Reroll ALL dice'),
            ('Garry', 'Operations',	'Reroll ALL dice'),
           ('Nauls', 'Operations', 'Reroll ALL dice')
             ''') """

c.execute('''
            INSERT INTO SCENARIO
            VALUES (5, 'Reveal all cards. If at least four have +1 dice value, you pass'),
            (3, 'Reveal all cards. If you have two fire extinguishers or two molotovs, you pass'),
            (4, 'Shuffle then reveal a random card. If it is a petri dish, you pass.'),
            (3, 'Reveal all cards. Roll dice equal to their total +dice value. If you get a 20+, you pass.'),
            (4, 'Shuffle then reveal a random card. If it has at least +1 dice value, you pass.'),
            (4, 'Reveal all cards. If you have an axe and a petri dish, you pass.'),
            (3, 'Reveal all cards. If at least three have exactly +1 dice value, you pass.'),
            (5,	'Shuffle then reveal a random card. If it is a Copper Wire, you pass.'),
            (5, 'Reveal all cards. If their total value is +7 dice or more, you pass.'),
            (3, 'Reveal all cards. Roll dice equal to their total +dice value. If you get a 3-die straight in two rolls, you pass.'),
            (5, 'Reveal all cards. Roll dice equal to their total +dice value. If you get a 22+, you pass.'),
            (3, 'Reveal all cards. If their total value is +4 dice or more, you pass.'),
            (4, 'Reveal all cards. If at least three are petri dishes, you pass.'),
            (3, 'Reveal all cards. Roll dice equal to their total +dice value. If you get a 18+, you pass.'),
            (4, 'Reveal all cards. If they all have +dice values of either +1 dice or +2 dice, you pass.'),
            (4, 'Reveal all cards. If at least four have exactly +1 dice value, you pass.'),
            (3, 'Reveal all cards. Roll dice equal to their total +dice value. If you get a 20+, you pass.'),
            (5,	'Shuffle then reveal a random card. If it is a knife, you pass.'),
            (5, 'Reveal all cards. If at least two have exactly +2 dice value, you pass.'),
            (3, 'Reveal all cards. If you have a gun, you pass.'),
            (5, 'Reveal all cards. Roll dice equal to their total +dice value. If you get a 24+, you pass.')
             ''')

""" c.execute('''
            INSERT INTO SUPPLY
            VALUES ('Axe', 1),
            ('Flashlight', 3),
            ('Copper Wire', 2),
            ('Knife', 0),
            ('Fire Extinguisher', 2),
            ('Petri Dish', 1),
            ('Flame Thrower', 1),
            ('Gun',	2),
            ('Molotov', 0)
             ''') """

""" c.execute('''
            INSERT INTO TILE
            VALUES (1, 'Dynamite'),
            (1, 'Thing'),
            (1, 'Rope'),
            (1, 'Dynamite'),
            (2, 'Thing'),
            (2, 'Thing'),
            (2, 'Rope'),
            (2,	'Dynamite'),
            (3, 'Thing'),
            (3, 'Rope'),
            (3, 'Dynamite')
            ''') """

conn.commit()
conn.close()