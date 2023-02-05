import socket
import sys

def eval_expression(expression,addr):
    try:
        print(f'Expression recieved from client {addr}: {expression}')
        return str(eval(expression))
    except:
        return "Invalid expression"

def server1(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen(1)
    print("Server1 started on port", port)
    conn, addr = server_socket.accept()
    server_socket.close()
    print("Client connected from", addr)
    while True:
        expression = conn.recv(1024).decode()
        if not expression:
            break
        result = eval_expression(expression,addr)
        conn.send(result.encode())
    conn.close()

if __name__ == "__main__":
    port = 1111
    server1(port)
