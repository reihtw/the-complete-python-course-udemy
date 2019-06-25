import logging

from app import books

logger = logging.getLogger('scraping.menu')


USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'bc' to look at the 5-star cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice:
>>> '''


def print_best_books():
    logger.info('Finding the best books by rating...')
    best_books = sorted(books, key=lambda x: (x.rating * -1))[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding the best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


def print_best_and_cheapest_books():
    logger.info('Finding the best books by rating and price...')
    best_and_cheapest_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_and_cheapest_books:
        print(book)


def next_book():
    for book in books:
        yield book

b = next_book()
def  print_next_book():
    global b
    try:
        logger.info('Getting next book from generator of all books...')
        print(next(b))
    except:
        logger.info('List of books has arrived to the final. Restarting the list...')
        print('No more books! Running the list again...')
        b = next_book()

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'bc': print_best_and_cheapest_books,
    'n': print_next_book
}

def menu():
    while True:
        choice = input(USER_CHOICE)

        if choice in ('b', 'c', 'bc', 'n'):
            user_choices[choice]()
        elif choice == 'q':
            break
        else:
            print('[-] Invalid option!')

    logger.debug('Terminating program...')

menu()
