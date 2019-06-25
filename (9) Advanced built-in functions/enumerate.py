top_friends = ['Marcus', 'Wrench', 'Sitara']

print(f'My top 1 friend is {top_friends[0]}.')
print(f'My top 2 friend is {top_friends[1]}.')
print(f'My top 3 friend is {top_friends[2]}.')

for i in range(3):
    print(f'My top {i+1} friend is {top_friends[i]}.')

for i, friend in enumerate(top_friends):
    print(f'My top {i+1} friend is {friend}.')

friend_g = enumerate(top_friends)
print(next(friend_g))