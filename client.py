import socket # import socket module
s = socket.socket()# create a socket object

host = socket.gethostname() # get local machine name
port = 12345 #reserve a port for your service

s.connect((host, port))

print(s.recv(1024))
s.close()
