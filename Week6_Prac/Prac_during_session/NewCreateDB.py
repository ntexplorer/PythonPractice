import sqlite3, os

def connect(filename):
    needcreate = not os.path.exists(filename)
    db = sqlite3.connect(filename)
    if needcreate:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, title TEXT NOT NULL, year INTEGER NOT NULL, author_id INTEGER NOT NULL, FOREIGN KEY (author_id) REFERENCES authors)")
        cursor.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT UNIQUE NOT NULL)")
        db.commit()
        cursor.close()
    return db

connect("books.db")

def add_author(db, name):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES ('{}')".format(name))
        db.commit()
        cursor.close()
    except sqlite3.IntegrityError:
        print ("The author exists already.")
    return

db = connect('books.db')
# add_author(db, 'J.R.R. Tolkien')
# add_author(db, 'Dan Brown')
# add_author(db, 'Dan Brown')

cursor = db.cursor()
cursor.execute("SELECT * FROM authors")
db.commit()
records = cursor.fetchall()
print(records)

cursor.execute("SELECT * FROM authors ORDER BY name ASC")
db.commit()
# select authors in alphabetic order
records = cursor.fetchall()
print(records)
cursor.close()

def browse_authors(db, byOrder=False):
    cursor = db.cursor()
    sql_st = "SELECT * FROM authors" if not byOrder else "SELECT * FROM autors ORDER BY name ASC"
    cursor,execute(sql_st)
    db.commit()
    records = cursor.fetchall()
    print("{:>4} | {:>16}".format('id', 'Author'))
    print("{0:->4} | {0:->16}".format(''))
    for item in records:
        print("{:>4} | {:>16}".format(item[0], item[1]))
        cursor.close()

# find the full solution on learning central
