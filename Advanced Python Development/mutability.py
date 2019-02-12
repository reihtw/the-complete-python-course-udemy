friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

# another_variable = friends_last_seen

print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0 # friends_last_seen.__setitem__('Rolf')

print(id(friends_last_seen))

my_int = 5

print(id(my_int))

my_int += 1 # my_int.__iadd__(self, 1): return cls(self.value + 1)

print(id(my_int))

friends = ['Rolf', 'Jose']
print(id(friends))

friends.append('Jen')
print(id(friends))

"""
integers
floats
strings
tuples
"""