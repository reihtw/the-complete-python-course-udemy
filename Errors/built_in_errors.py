# * IndexError
'''
>>> friends = ['Rolf', 'Anne']
>>> friends[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
IndexError: list index out of range
'''

# * KeyError
'''
def show_movie_details(movie):
    print(f'Name: {movie['name']'})
    print(f'Director: {movie['director']'})
    print(f'Release year: {movie['release']}') -> It should be 'year'

Traceback (most recent call last):
    ...
KeyError: 'release'
'''

# * NameError
'''
>>> print(my_variable)
Traceback (most recent call last):
  File ".\intro.py", line 1, in <module>
    print(my_variable)
NameError: name 'my_variable' is not defined
'''

# * AttributeError
'''
>>> friends = ['Rolf', 'Jose', 'Charlie']
>>> friends_nearby = ['Rolf', 'Anna']
>>> friends.intersection(friends_nearby)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module> 
AttributeError: 'list' object has no attribute 'intersection'
'''

# * NotImplementedError
'''
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        raise NotImplementedError('This feature has not been implemented yet.')
'''

# * RuntimeError
'''
?
'''

# * SyntaxError
'''
class User <- The collon is missing
    def __init__(self, username, password):
        self.username = username
        self.password = password
'''

# * IndentationError
'''
def add_two(x,y):
return x + y
'''

# * TabError
'''
def add_two(x,y):
    return x + y # spaces

def pow(n, exp):
    return n ** exp # tabs
'''

# * TypeError
'''
>>> 5 + 5
10
>>> 'hi' + 'ha'
'hiha'
>>> 5 + 'hi'
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

# * ValueError
'''
>>> int('20.5')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '20.5'
'''

# * ImportError
'''
# app.py
import blog

def menu():
    pass

# blog.py
from app import menu

def do_something():
    pass
'''

# * DeprecationWarning
'''
from database import Database

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def register(self):
        Database.write(self.username, self.password)
        raise DeprecationWarning('User#register still works, but is deprecated.')
    
    @classmethod
    def register_user(cls, username, password):
        Database.write(username, password)
        return cls(username, password)
'''


# BUT...
# - often you won't be raising any of these exceptions
# - you should create your own exceptions, with even better names!