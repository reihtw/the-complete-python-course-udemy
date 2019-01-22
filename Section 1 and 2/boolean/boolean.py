# Boolean and comparisons in python

truthy = True
falsy = False

# comparison signals
age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20 

# string isn't equal a integer
my_number = 5
user_number = input('Enter a number: ')

print(my_number == user_number)
print(my_number != user_number) # is not equal comparance

yes = True and True
no = True and False

print(no)

which_one_is_it = True or False # first one
second_one = False or True
whatever_one = True or True