import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

top_player_name = players[0]['name'] 
top_player_score = 0

for player in players:
    number_matched = player['numbers'] & lottery_numbers
    score = 100 ** len(number_matched)
    if score > top_player_score:
        top_player_score = score
        top_player_name = player['name']

print('{} won {}'.format(top_player_name, top_player_score))
