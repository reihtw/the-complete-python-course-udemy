from utils import database

USER_CHOICE= """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    while True:
        user_input = input(USER_CHOICE)
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        elif user_input == 'q':
            print('\n[*] Bye...\n')
            break
        else:
            print('[-] Invalid command! Insert a valid command.')


def prompt_add_book():
    name = input('Insert the book name: ')
    author = input('Insert the author name: ')
    database.add_book(name, author)


def list_book():
    books = database.list_book()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f'''
name: {book['name']}
author: {book['author']}
read: {read}
        ''')

def prompt_read_book():
    name = input('Please, insert the name of the book to mark as read: ')
    print(database.read_book(name))


def prompt_delete_book():
    name = input('Please inset the name of the book to delete: ')
    database.del_book(name)


if __name__ == "__main__":
    menu()