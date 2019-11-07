sql_create_tb_books = "CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, title TEXT NOT NULL, year INTEGER NOT NULL, author_id INTEGER NOT NULL, FOREIGN KEY (author_id) REFERENCES authors)"

sql_create_tb_author = "CREATE TABLE authors (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL. name TEXT UNIQUE NOT NULL)"

import sqlite3

db = sqlite3.connect('./dbs/books.db')

cursor = db.cursor()

cursor.execute(sql_create_tb_author)

cursor.execute(sql_create_tb_books)

db.commit()
