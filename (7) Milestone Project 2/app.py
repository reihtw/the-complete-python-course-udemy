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
            name = input('Insert the book name: ')
            author = input('Insert the author name: ')
            prompt_add_book(name, author)
        elif user_input == 'l':
            list_book()
        elif user_input == 'r':
            name = input('Please, insert the name of the book to mark as read: ')
            print(prompt_read_book(name))
        elif user_input == 'd':
            name = input('Please inset the name of the book to delete: ')
            prompt_delete_book(name)
        elif user_input == 'q':
            print('\n[*] Bye...\n')
            break
        else:
            print('[-] Invalid command! Insert a valid command.')

def prompt_add_book(name, author):
    database.add_book(name, author)

def list_book():
    database.list_book()

def prompt_read_book(name):
    return database.read_book(name)

def prompt_delete_book(name):
    database.del_book(name)

if __name__ == "__main__":
    menu()