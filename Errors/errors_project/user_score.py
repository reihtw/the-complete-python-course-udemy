class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
    
    def __repr__(self):
        return f'<User {self.name}>'

def email_engaged_user(user):
    try:
        perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorret values provided to our calculation function.')
    else:
        send_engagement_notification(user)

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f'Notification sent to {user}')

my_user = User('Rolf', {'click': 61, 'hits': 100})
get_user_score(my_user)
