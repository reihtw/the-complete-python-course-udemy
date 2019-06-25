# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json

teams = []
csv_file = open('csv_file.csv', 'r')
csv = [line.strip() for line in csv_file.readlines()]
csv_file.close()

for line in csv:
    club, city, country = line.split(',')
    team_ad = {'club': club, 'country': country, 'city': city}
    teams.append(team_ad)

json_file = open('json_file.json', 'w')
json.dump(teams, json_file)
json_file.close()
    