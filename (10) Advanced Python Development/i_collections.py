"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque

The main purpose od this video is to make you aware that these things exist,
in case we have to use them later on (or when you encounter a situation where
using one of these would be useful).

Normally what happens in those situations is we struggle to build our own thing
to do what we nees it to do. Knowing that these exist could save you a lot of
effort!

"""

## Counter
"""
Allow us to count things. Give it a iterable or a mapping (such as a dict) and
ir will turn into a counter of elements.
"""
from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

## defaultdict
"""
The 'defaultdict' never raises a 'KeyError'. Instead, it returns the value returned
by the function spcified when the object was instantied.
"""
from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

print(alma_maters['Rolf'])
print(alma_maters['Anne'])

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company
print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])

## ordereddict - useless but is good to know that it exists
from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)
o.move_to_end('Rolf')
print(o)
o.move_to_end('Jen', last=False)
print(o)
o.popitem()
print(o)

#namedtuple
"""
A namedtuple is another object that we can use like a tuple, where each of the elements of the tuple has a name. In addition, the tuple itself also has a name.

It improves on tuples by making more explicit what it means.
"""

from collections import namedtuple

account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850)
print(account.name)

print(account)

accountNamedTuple = Account(*account)

print(accountNamedTuple._asdict())

#deque
from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
friends.popleft()

print(friends)
