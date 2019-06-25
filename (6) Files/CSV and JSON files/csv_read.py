csv_file = open('csv_data.txt', 'r')
csv = [line.strip() for line in csv_file.readlines()[1:]]
csv_file.close()

for line in csv:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')
