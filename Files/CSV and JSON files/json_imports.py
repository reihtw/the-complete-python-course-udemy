import json

file_json = open('friends_json.txt', 'r')
file_contents = json.load(file_json) # reads file and turns it to dictionary

file_json.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

# Go and investigate how to use json.dump
'''
json_string = json.dumps(cars)
print(len(list(json_string)))
'''

with open('data_file.json', 'w') as write_file:
    json.dump(cars, write_file)

my_json_string = '[{"name": "Alfa Romeo", "released":1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])