primes = [2, 3, 5, 7, 11]

for prime in primes:
    print(f'{prime} is a prime number')

kid_ages = (3, 7, 12)
for age in kid_ages:
    print(f'I have a {age} year old kid.')

for i in range(20):
    print(i)

print(range(10))

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}

for name, days in my_friends.items():
    print(f'I last saw {name} {days} days ago.') 
print(my_friends.items()) # [('Jose', 6), ('Rolf', 12), ('Anne', 6)]

for t, i in [('Jose', 6), ('Rolf', 12), ('Anne', 6)]:
    print(t)
    print(i)
