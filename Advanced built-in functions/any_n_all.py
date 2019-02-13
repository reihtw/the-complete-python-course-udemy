friends = [
    {
        'name': 'Marcus Holloway',
        'location': 'San Francisco'
    },
    {
        'name': 'Aiden Pierce',
        'location': 'Chicago'
    },
    {
        'name': 'Elliot Alderson',
        'location': 'New York City'
    },
    {
        'name': 'Michael de Santa',
        'location': 'Los Angeles'
    },
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby): # True if there's at least one; or false if empty
    print('You are not alone!')

print(all([1, 2, 3, 4, 5, 0])) # True if all values are True.
"""
* 0, 0.0
* None
* [], (), {}
* False
All these values are false.
"""