


import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((socket.gethostname(),1234))
# s.listen(5)

# while True:
#     clientsocket,address = s.accept()
#     print(f"connection from {address} has been estalished!") 
#     clientsocket.send(bytes('welcome to the server!'),"utf-8")
#     clientsocket.close()


s = socket.socket() 
print('socket succesfully created') 
port = 12345 
s.bind(('', port))
print(f'socket binded to port{port}') 
s.listen(5)
print('socket is listening') 
while True: 
    c,addr = s.accept() 
    print('got connection from ',addr) 
    message  = ('thank you for connecting ') 
    c.send(message.encode()) 
    c.close() 