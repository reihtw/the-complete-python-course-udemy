friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.starswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))

friends_lower = map(lambda x: x.lower(), friends) # is the same of this friends_lower = (friends.lower() for friend in friends)
print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

user = [
    {'username': 'defalt', 'password':'idontknow'},
    {'username': 'dusan', 'password': 'ihatededsec'}
]

users = [User.from_dict(user) for user in user]
users = map(User.from_dict, user)
