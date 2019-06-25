friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

def see_friend(friends, name):
    print(f'friends_last_seen id (inside the function): {id(friends)}')
    friends[name] = 0

print(f'friends_last_seen id (before function): {id(friends_last_seen)}')
print(f"friends_last_seen['Rolf'] id (before function): {id(friends_last_seen['Rolf'])}")
see_friend(friends_last_seen, 'Rolf')
print(f"friends_last_seen['Rolf'] id (after function): {id(friends_last_seen['Rolf'])}")
print(f'friends_last_seen id (after function): {id(friends_last_seen)}')

#--------

age = 20

def increase_age(current_age):
    current_age = current_age + 1

print(f'age id (before function): {id(age)}')
increase_age(age)
print(f'age id (after function): {id(age)}')

#---------

primes = [2, 3, 5]

print(f'prime numbers id: {id(primes)}')

primes += [7, 11]

print(f'prime numbers id (with 7 and 11): {id(primes)}')