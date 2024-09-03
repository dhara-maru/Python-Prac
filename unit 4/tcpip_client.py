import socket

def start_client(host, port):
   
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        
        client_socket.connect((host, port))
        print(f"Connected to the server at {host}:{port}")

     
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received message from the server: {message}")

    finally:
    
        client_socket.close()
        print("Connection closed with the server.")

server_host = "127.0.0.1" 
server_port = 12345

start_client(server_host, server_port)
