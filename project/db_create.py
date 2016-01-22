from views import db
from models import Task
from datetime import date

# create teh database and the db table
db.create_all()

# insert data
# db.session.add(Task("Finish this tutorial", date(2016, 1, 21), 10, 1))
# db.session.add(Task("Finish Real Python", date(2016, 2, 3), 10, 1))

# commit the changes
db.session.commit()

# CONFIG FOR SQLITE3
# import sqlite3
# from _config import DATABASE_PATH
#
# with sqlite3.connect(DATABASE_PATH) as connection:
#
#     #get cursor
#     c = connection.cursor()
#
#     #create the table
#     c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY
#         AUTOINCREMENT,
#         name TEXT NOT NULL, due_date TEXT NOT NULL, priority
#         INTEGER NOT NULL,
#         status INTEGER NOT NULL)""")
#
#     #insert dummy data
#     c.execute('INSERT INTO tasks (name, due_date, priority, status)'
#         'VALUES("Finish this tutorial", "01/16/2016", 10, 1)')
#     c.execute('INSERT INTO tasks (name, due_date, priority, status)'
#         'VALUES("Finish Real Python Course 2", "02/03/2016", 10, 1)')
#
