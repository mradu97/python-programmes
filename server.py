import socket #import socket module
s = socket.socket() # create a socket object
host = socket.gethostname() # get local machine name
port = 12345 #reserve a port for your service
s.bind((host,port)) # bind to the port
s.listen(5) # now wait for client connection
while True:
    c, addr = s.accept()#establish connection with client.
    print('got connection from',addr)
    x = [2,3,4]
    byt = bytes(x)
    c.send(byt)
    c.close()
