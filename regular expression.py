
# import re
# text = '''elon- musk phone number is 9999111125666, call him if you have- any questions 
# on dodgecoin.TESLA revenue .tesla cfo number (9999)-(5555)-(44545)'''
# # match = re.match(pattern,string,<flag = 0>)
# # match = re.match(r'\w+',text)
# match = re.search(r'\w+',text)
# print(match)

import re
email = input('whats your email?').strip() 
# pattern = r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.edu$'
pattern = r'\w+@(\w+\.)?\w+\.edu$'
if re.search(pattern,email,re.IGNORECASE):
    print('vaild')
else:
    print('invalid')

# import re
# user = input('enter your name:').strip() 
# if matches := re.search(r'(.+),(.+)',user):

#     last,first = matches.groups() 
#     user = f'{first} {last}'
# print('hello',user)

# import re
# url = input('enter url:').strip() 
# username = re.findall(r'^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_-]+)$',url,re.IGNORECASE)
# if username:
#     print('valid url')
#     print(username)   
# else:
    # print('invalid url') 
# user = input('enter ur email address: ')
# if p := re.findall(r'^\w+[^@]+@[^@]\w+\.(edu|com|org|gov)$',user,re.IGNORECASE):
#     print('vaild email')
# else:
#     print('invalid email')
    
# user = input('enter your email address:')
# if p := re.findall(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$',user):
#     print('valid email')
# else:
#     print('invalid email')
# import time 
# start = time.time() 
# d = {'tom':34,'hand':56,'pat':67}
# p = {k: v for (k,v) in d.items() if v >= 50}
# ends = time.time() 
# print(ends - start)
# print(p)

