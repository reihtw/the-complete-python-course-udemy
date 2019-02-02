import json

"""
Concerned with storing and retrieving books from a list.
"""

books_file = 'books.json'


def add_book(name, author):
        books = list_book()
        books.append({'name': name, 'author': author, 'read': False})
        save_all_books(books)


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