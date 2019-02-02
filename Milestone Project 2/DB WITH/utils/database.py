import sqlite3

"""
Concerned with storing and retrieving books from a list.
"""


def create_book_table():
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

        connection.commit()
        connection.close()

def add_book(name, author):
        # *,0); DROP TABLE books; -> SQL Injection Vulnerability if change strings directly
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

        connection.commit()
        connection.close()


def list_book():
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # [(name, author, read), (name, author, read)]

        connection.close()
        return books      


def read_book(name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

        connection.commit()
        connection.close()

def del_book(name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))

        connection.commit()
        connection.close()
