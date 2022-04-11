import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "Create table if Not EXISTS book(id INTEGER Primary Key,title TEXT,author TEXT,year Integer,Price Integer)")
    conn.commit()
    conn.close()


# connect()


def insert(title, author, year, price):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("Insert into book Values(NULL,?,?,?,?)",
                (title, author, year, price))
    conn.commit()
    conn.close()


# insert("ABC", "author1", 2022, 100)


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("Select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows


print(view())


def search(title="", author="", year="", price=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("Select * from book where title=? or author=? or year=? or price=?",
                (title, author, year, price))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("Delete from book where id=?", (id,))
    conn.commit()
    conn.close()


def update(title, author, year, price, id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("Update book set title=?,author=?, year=?,price=? where id=?",
                (title, author, year, price, id))
    conn.commit()
    conn.close()
