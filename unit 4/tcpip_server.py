import socket

def start_server(host, port):
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
   
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
       
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Connection established from {client_address}")

       
        message = "Hello, client! This is the server."
        client_socket.sendall(message.encode('utf-8'))

       
        client_socket.close()
        print("Connection closed with the client.")

server_host = "127.0.0.1"  # Loopback address for local testing
server_port = 12345

start_server(server_host, server_port)
