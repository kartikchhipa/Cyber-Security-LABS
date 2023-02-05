import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

print("Enter the host address: ",end='')
# server's IP address
host = input()

# server's port
port = 80 

# connect to the server
s.connect((host, port))

print("connected")

s.sendall(b'GET / HTTP/1.1\r\n\r\n')



# receive data from the server
data = s.recv(1024)

print(data.decode())



# close the sockett
s.close()
