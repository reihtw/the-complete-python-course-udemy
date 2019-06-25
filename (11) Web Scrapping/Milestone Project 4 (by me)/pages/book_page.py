from bs4 import BeautifulSoup

from locators.book_page_locator import BookPageLocators
from parsers.book import BookParser

class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def books(self):
        locator = BookPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]
    