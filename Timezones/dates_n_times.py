from datetime import datetime, timezone, timedelta

print(datetime.now())

print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(f'Today: {today}')
print(f'Tomorrow: {tomorrow}')

print(today.strftime('%d-%m-%Y %H:%S'))

user_date = input('Enter the date in yyyy-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d') #string parse time
print(user_date)