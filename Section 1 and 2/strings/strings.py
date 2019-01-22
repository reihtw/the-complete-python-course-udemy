my_string = "Hello, world!"
single_quote_string = 'Hello, world!'

# strings: a sequence of characters that, don't necessarily, make sense to the computer.
# use:	   strings are almost always used to output stuff, that is, messages to show to user, for example.
# quotes:  you can use a single quote to create strings, or double quote. This doesn't make difference.

## Case when you have a quote in a string

string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing!" yesterday.'

# The recommendadtion is use the reverse quotes at the points of the string.
# But, it has one more way to do this:

escaped_quotes = "He said \"You are amazing!\" yesterday."
# But, it isn't recommended

##-------

name = 'Rodrigo'
greeting = 'Hello, ' + name
# simple way to concatenate a string to a variable

another_greeting = f'Hello, {name}'
# this is a new form to formats strings (3.6.x or above)

# OLD FORM TO FORMAT STRINGS
final_greeting = 'How are you, {}'.format(name)
