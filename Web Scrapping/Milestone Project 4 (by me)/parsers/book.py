from locators.book_locators import BookLocators

class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Book: {self.name}: €{self.price} | Stock: {self.stock}'
    
    @property
    def name(self):
        locator = BookLocators.NAME
        return self.parent.select_one(locator).attrs['title']
    
    @property
    def price(self):
        locator = BookLocators.PRICE
        return self.parent.select_one(locator).string
    
    @property
    def stock(self):
        locator = BookLocators.STOCK
        return self.parent.select_one(locator).string