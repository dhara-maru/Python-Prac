import socket

def start_file_server(host, port):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))
    print(f"File Server listening on {host}:{port}")

    server_socket.listen(1)

    while True:
        
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Connection established from {client_address}")

        try:
          
            file_name = client_socket.recv(1024).decode('utf-8')
            print(f"Received file request: {file_name}")

          
            try:
                with open(file_name, 'rb') as file:
                    file_content = file.read()
               
                client_socket.sendall(file_content)
                print(f"File content sent to {client_address}")
            except FileNotFoundError:
                error_message = "File not found on the server."
                client_socket.sendall(error_message.encode('utf-8'))
                print(f"Error: {error_message}")

        finally:
            
            client_socket.close()
            print("Connection closed with the client.")

file_server_host = "127.0.0.1"  # Loopback address for local testing
file_server_port = 12345

start_file_server(file_server_host, file_server_port)
