from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a list.
"""


def create_book_table():
        with DatabaseConnection('data.db') as cursor:
                cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name, author):
        # *,0); DROP TABLE books; -> SQL Injection Vulnerability if change strings directly
        with DatabaseConnection('data.db') as cursor:
                cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def list_book():
        with DatabaseConnection('data.db') as cursor:
                cursor.execute('SELECT * FROM books')
                books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # [(name, author, read), (name, author, read)]

        return books      


def read_book(name):
        with DatabaseConnection('data.db') as cursor:
                cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def del_book(name):
        with DatabaseConnection('data.db') as cursor:
                cursor.execute('DELETE FROM books WHERE name=?', (name,))
