class Database:
    content = {'users': []}

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)
    
    @classmethod
    def remove(cls, username):
        cls.content['users'] = [user for user in cls.content['users'] if user['username'] == username]
    
    @classmethod
    def find_by_username(cls, username):
        return [user for user in cls.content['users'] if user['username'] == username]
    
    @classmethod
    def find_by_access(cls, access):
        return [user for user in cls.content['users'] if user['access'] == access] 