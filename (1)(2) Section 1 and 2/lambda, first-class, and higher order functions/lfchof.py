def add_two(x, y):
    return x + y

add_two(10, 5)

lambda x, y: x+y
print((lambda x, y: x+y)(10, 5))

add = lambda x, y: x+y

def who(data, identify):
    return identify(data)

def my_identifier_function(some_data):
    return some_data['name']

user = {'name':'Antares', 'surname':'Lucius'}

print(who(user, my_identifier_function))
print(who(user, lambda x: x['name']))
