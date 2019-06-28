from admin import Admin
from user import User
from database import Database

a = Admin('dusan', '1234', 3)
u = User('defalt', 'rat')

users = [a, u]
for user in users:
    user.save()
    print(Database.find_by_username(user.username))
