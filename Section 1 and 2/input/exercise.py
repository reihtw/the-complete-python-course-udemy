# exercise - input
# show total of seconds lived

age = int(input('Enter your age: '))

days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f'You have lived {seconds} seconds.')