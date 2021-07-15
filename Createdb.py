import sqlite3

with sqlite3.connect('todo.db') as db:
    cursor = db.cursor()
cursor.execute(
    '''
    CREATE TABLE "items" (
    "item" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    PRIMARY KEY("item")
);   
    ''')