numbers = list(range(10))
doubled_numbers = [n*2 for n in numbers]
#for num in numbers:
#    doubled_numbers.append(num * 2)

phrases = [f'I am {age} years old.' for age in doubled_numbers]

#print(phrases)

names_list = ['John', 'Rolf', 'Anne']
lowercase_names = [name.lower() for name in names_list]

#friend = input('Enter your friend name: ')
#print(friend.lower() in lowercase_names)

## With conditional

evens = [n for n in numbers if n % 2 == 0]


friends = ['rolf', 'ruth', 'charlie']
guests  = ['Jose', 'Rolf', 'ruth', 'Charlie', 'michael']

lower_friends = [n.lower() for n in friends]

# present_friends = [friend for friend in friends for guest in guests if friend == guest.lower()]
present_friends = [name.capitalize() for name in guests if name.lower() in lower_friends]
#print(present_friends)

friends = {'rolf', 'anna', 'charlie'}
guests  = {'jose', 'rolf', 'ruth', 'charlie', 'michael'}

present_friends = {name.capitalize() for name in guests if name in friends}
present_friends = friends & guests
present_friends = {name.capitalize for name in friends & guests}
#print(present_friends)

names = ['Rolf', 'Anna', 'Charlie']
time_last_seen = [10, 15, 8]

friends_last_seen = {names[i]: time_last_seen[i] for i in range(len(names))}
print(friends_last_seen)

friends_last_seen = dict(zip(names, time_last_seen)) # zip | [('Rolf', 10), ('Anna', 15), ('Charlie', 8)]