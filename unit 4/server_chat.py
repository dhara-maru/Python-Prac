import socket
import threading

def handle_client(client, addr):
    while True:
        message = client.recv(1024).decode('utf-8')
        if not message: break
        print(f"Received from {addr}: {message}")
        [c.sendall(message.encode('utf-8')) for c in clients if c != client]

    clients.remove(client)
    client.close()
    print(f"Connection closed with {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(5)

print("Chat server listening on port 12345")

clients = []

try:
    while True:
        client, addr = server.accept()
        print(f"Connection established with {addr}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client, addr)).start()

except KeyboardInterrupt:
    print("Server terminated.")
    server.close()
