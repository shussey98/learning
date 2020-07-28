from datetime import datetime, timezone, timedelta


#naive dt object
print(datetime.now())

#aware dt object
print(datetime.now(timezone.utc))

today  = datetime.now(timezone.utc)
tomorrow = today + timedelta(days = 1)

print(today)
print(tomorrow)

print(today.strftime('%d-%m'))

user_date = input('Enter date YYYY-mm-dd: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d') #string parse time

print(user_date)

