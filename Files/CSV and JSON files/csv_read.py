csv_file = open('csv_data.txt', 'r')
csv = [line.strip() for line in csv_file.readlines()]

csv_file.close()