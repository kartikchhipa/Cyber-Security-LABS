import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        if data.islower():
            c.send(data.upper().encode())
        else:
            c.send(data[::-1].encode())
        print("data received from the client is: " + str(data))
    c.close()

if __name__ == '__main__':
    main()
