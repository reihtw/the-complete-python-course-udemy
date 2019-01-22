# Getting user input in Python

my_name = 'Rodrigo'
your_name = input('Enter your name: ')

# sometimes you will have to ask the user something and the function input() do that.
# the function input() works like the function print(), because it prints something in the screen too. But, it waits to user type something and press [ENTER].

age = int(input('Enter your age: '))
# when you ask some number to the user, you have to convert it into a integer (or float), because if you don't, the computer will treat like a string.

print(f'You have lived {age * 12} months.')
# to facilitate the compreension it's recommended you  put the [age * 12] in a variable.