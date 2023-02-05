import socket
import os
import sys
def eval_expression(expression,addr):
    try:
        print(f'Expression recieved from client {addr}: {expression}')
        return str(eval(expression))
    except:
        return "Invalid expression"

def handle_client(conn, addr):
    print("Client connected from", addr)
    while True:
        expression = conn.recv(1024).decode()
        if not expression:
            break
        result = eval_expression(expression,addr)
        conn.send(result.encode())
    conn.close()

def server2(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen(5)
    print("Server2 started on port", port)
    while True:
        conn, addr = server_socket.accept()
        pid = os.fork()
        if pid == 0:
            server_socket.close()
            handle_client(conn, addr)
            os._exit(0)
        else:
            conn.close()

if __name__ == "__main__":
    port = 1111
    server2(port)
