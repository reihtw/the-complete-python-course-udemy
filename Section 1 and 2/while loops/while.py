is_programmer = False
while not is_programmer:
    print('Learn programming ')
    user_is_programmer = input('Are you a programmer yet? ')
    is_programmer = user_is_programmer == 'yes'

i = 0
while i < 10:
    print(f'Repeated {i} times.')
    i += 1

temperature = 15

while temperature < 20:
    print('Heating...')
    temperature += 1
