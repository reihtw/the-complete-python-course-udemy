"""
Concerned with storing and retrieving books from a list.
"""

books = []

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})

def list_book():
    for book in books:
        print(f'''
name: {book['name']}
author: {book['author']}
read: {'Yes' if book['read'] else 'No'}
        ''')

def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            return f"[*] The book \"{book['name']}\" was marked as read."
    return '[-] The book was not found.'

def del_book(name):
    i = 0
    for book in books:
        if book['name'] == name:
            books.pop(i)
            return '[*] The book was deleted successfuly.'
    return '[-] The book was not found.'