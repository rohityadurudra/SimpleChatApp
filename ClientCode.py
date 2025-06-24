import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
USERNAME = input("Enter your name: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print("\n" + message)
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg_body = input("You: ")
    if msg_body.lower() == 'exit':
        break
    message = f"MSG|{USERNAME}|{msg_body}\n"
    client_socket.sendall(message.encode())

client_socket.close()
