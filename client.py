import socket 
s = socket.socket()
port  = 12345
s.connect(('',port))
print(s.recv(1024))
s.close() 
# s.connect((socket.gethostname(), 1234)) 

# msg = s.recv(1024)
# print(msg.decode("utf-8"))