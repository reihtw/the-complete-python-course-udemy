# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

import codecs

friends = []
for f in range(3):
    friend = input(f'Type a name of the {f+1} friend: ')
    friends.append(friend)

file_nearby = codecs.open('nearby_friends.txt', 'w', 'utf8')
file_people = codecs.open('people.txt', 'r', 'utf8')
line_people = [line.strip() for line in file_people.readlines()]
for line in line_people:
    for friend in friends:
        if line == friend:
            file_nearby.write(f'{friend}\n')

file_people.close()            
file_nearby.close()

file_nearby = codecs.open('nearby_friends.txt', 'r', 'utf8')
file_n = file_nearby.readlines()
for friend in file_n:
    friend = friend.replace('\n', '')
    print(f'{friend} is nearby! Meet up with them.')
file_nearby.close()

'''
CORRECTION CODE:

friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

peoples = opem('people.txt', 'r')
people_nearby = people.readlines()

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_Set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet with them.')
    nearby_friends_file.write(f'{friend}')

nearby_friends_file.close()
'''