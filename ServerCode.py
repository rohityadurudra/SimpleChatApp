import socket

HOST = '127.0.0.1'  # Localhost
PORT = 5000         # TCP Port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server running on {HOST}:{PORT}")

clients = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            client.sendall(message.encode())

while True:
    conn, addr = server_socket.accept()
    clients.append(conn)
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        decoded = data.decode().strip()
        print(f"Received: {decoded}")
        broadcast(decoded, conn)

    conn.close()
    clients.remove(conn)
    print(f"Disconnected: {addr}")
