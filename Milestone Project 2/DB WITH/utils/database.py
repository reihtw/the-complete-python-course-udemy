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
        # *,0); DROP TABLE books;
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

        connection.commit()
        connection.close()


def list_book():
        with open('books.json', 'r') as file_json:
                return json.load(file_json)        


def read_book(name):
        books = list_book()
        for book in books:
                if book['name'] == name:
                        book['read'] = True
                        return f"[*] The book \"{book['name']}\" was marked as read."
        return '[-] The book was not found.'


def del_book(name):
        books = list_book()
        books = [book for book in books if book['name'] != name]
        save_all_books(books)


#def del_book(name):
#    i = 0
#    for book in books:
#        if book['name'] == name:
#            books.pop(i)
#            return '[*] The book was deleted successfuly.'
#    return '[-] The book was not found.'


def save_all_books(books):
        with open('books.json', 'w') as book:
                json.dump(books, book)