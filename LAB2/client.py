import socket
import sys
def client(port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", port))
    except ConnectionRefusedError as e:
        print(f'Another client is already connected: {e}')
        return 
    while True:
        expression = input("Enter an arithmetic expression: ")
        client_socket.send(expression.encode())
        result = client_socket.recv(1024).decode()
        print("Result:", result)

if __name__ == "__main__":
    port = 1111
    client(port)

