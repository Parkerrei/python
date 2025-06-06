# import socket 
# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/romeo.txt, HTTP/1.0\n\n'.encode() 
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break 
#     print(data.decode())
# mysock.close()

# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('www.youtube.com',80))
# cmd = 'GET /romeo.txt,HTTP/1.1\r\nHost:www.youtube.com\r\n\r\n'.encode() 
# mysock.send(cmd) 

# while True:
#     data = mysock.recv(512) 
#     if len(data) <1:
#         break 
#     print(data.decode()) 
# mysock.close() 

# import urllib.request
# urllib.parse
# urllib.error
# count = dict()
# fhand = urllib.request.urlopen('http://www.google.com')

# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         count[word] = count.get(word,0) + 1
# print(count)

# import urllib.request 
# import urllib.parse
# import urllib.error
# import bs4
# import ssl 
# ctx = ssl.create_default_context() 
# ctx.check_hostname = False 
# ctx.verify_mode = ssl.CERT_NONE 

# url = input('enter - ') 
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = bs4.BeautifulSoup(html, 'html.parser') 
# tags = soup('a') 
# for tag in tags:
#     print(tag.get('href',None)

# import json 
# data = '''{"name": "peter","phone":{"type":"intl","number":918729970834},"email": {"hide": "yes"}}'''
# info = json.loads(data) 
# print(info)
# print(info['name'])
# k = info.setdefault('job','programmer')
# print(info )

# input = '''[{"id": "001",
# "x": "2",
# "name": "peter" },
# {"id":"008",
# "x":"8",
# "name": "peter"
# }
# ]'''

# info = json.loads(input) 
# print('user count :', len(info)) 
# for item in info: 
#     print('name', item['name']) 
#     print('id', item['id']) 
#     print('attribute', item['x']) 


# import the module socket for creating webbrowser object 
# import socket

# # create a socket object
# my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# # connect the server  
# my_socket.connect(('data.pr4e.org',80)) 

# # send an http Get request 
# cmd = 'GET http://data.pr4e.org/romeo.txt http/1.0'.encode()
# my_socket.send(cmd) 

# # receive and display the response
# while True:
#     data = my_socket.recv(512) 
#     if len(data) < 1 :
#         break 
#     print(data.decode() ,end  = '') 
    
# # close the socket 
# my_socket.close() 

# import requests

# # Define the API endpoint
# url = 'https://www.google.com/entries'

# # Make the GET request
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f'Error: {response.status_code}')

# import requests
# r = requests.get('https://api.github.com/user',auth =('user','pass'))
# # r.status_code
# # r.headers['content-type']
# r.encoding
# r.json()
# r.text
# print(r)
