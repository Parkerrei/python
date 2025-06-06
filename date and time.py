# import datetime

# specific_date = datetime.datetime(2024 , 11 , 8 , 22, 23, 0) 
# print(specific_date)
# c_time = datetime.datetime.now()
# formatted = c_time.strftime('%H %M %S %B')
                                  
# print(formatted)
# print(c_time)

# parsing date and times
# date_string = '2024-04-22 3:45:00'
# parsed_date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
# print(parsed_date) 

# calculating difference between dates 
# date1 = datetime.datetime(2024,3,9)
# date2 = datetime.datetime(2000,9,22)
# difference = date2 - date1 
# print(difference.days)

# calculate age 
# import datetime
# def calculate_age(birthdate):
#     today = datetime.datetime.today() 
#     age   = today.year - birthdate.year 
#     if (today.month,today.day) < (birthdate.month,birthdate.day):
#         age -= 1
#     return age 
# birthday  = datetime.datetime(2000,9,22)
# age       = calculate_age(birthday)
# print(f'you are now {age} yrs old')

# import datetime
# import time

# while True:
#     current_time = datetime.datetime.now().strftime("%b:%M:%S")
#     print(current_time, end="\r")
#     time.sleep(1)

# import datetime
# def calculate_age(user):
#     date = datetime.datetime.now().month
#     return user  - date
# try:
#     user = int(input('enter your date of birth:'))
#     age = calculate_age(user) 
#     print(f'your age is :{age}') 
# except ValueError:
#     print('enter a valid year') 

# now = datetime.datetime.now()
# print(now) 

# print(now.hour) 
# print(now.minute)
# print(now.second) 
# print(now.year) 
# print(now.month) 
# print(now.day)

# import datetime

# def your_age(birthdate):
#     now = datetime.date.today()
#     age = now.year - birthdate.year
#     if (now.month,now.day) < (birthdate.month,birthdate.day) :
#         age -= 1 
#     return age 

# try:
#     user  = input('enter your date of birth in (dd-mm-yyyy):')
#     birthdate = datetime.datetime.strptime(user,'%d-%m-%Y').date()
#     age = your_age(birthdate)
#     print(f'you are {age} yrs old')
# except ValueError:
#         print('enter valid date of birth:') 

# get_age = datetime.datetime.today() 
# user    = input('enter your date of birth : (dd-mm-yyyy)')

# k   =  datetime.datetime.strptime(user,'%d-%m-%Y').date() 
# age = get_age.year - k.year 
# print(f'you are {age} yrs old') 

# import datetime 
# today_date = datetime.datetime.today() 
# user = input('enter your date of birth:(dd-mm-yyyy)') 
# format_user = datetime.datetime.strptime(user,'%d-%m-%Y').date() 
# difference = today_date.year - format_user.year
# print(difference)
# print(difference)

# today_date  = datetime.datetime.today()
# user = input('enter your date of birht:(dd-mm-yyyy)')
# parse_date = datetime.datetime.strptime(user,'%d-%m-%Y')
# difference = today_date - parse_date 
# print(difference)

from dateutil.relativedelta import relativedelta
import datetime

now_1 = datetime.date.today() 
month_later = now_1 + relativedelta(months = 2, days = 10) 
format = month_later.strftime('%A-%b-%Y')
print(format)

