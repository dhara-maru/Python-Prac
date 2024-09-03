import socket

def start_file_client(server_host, server_port, file_name):
 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
       
        client_socket.connect((server_host, server_port))
        print(f"Connected to the File Server at {server_host}:{server_port}")

        client_socket.sendall(file_name.encode('utf-8'))
        print(f"File request sent to the server: {file_name}")

        file_content = client_socket.recv(1024)

        if file_content[:5] == b'Error':
            print(f"Error from server: {file_content.decode('utf-8')}")
        else:
            
            with open(f"received_{file_name}", 'wb') as received_file:
                received_file.write(file_content)
                print(f"File content saved to received_{file_name}")

    finally:
       
        client_socket.close()
        print("Connection closed with the server.")

file_server_host = "127.0.0.1"  
file_server_port = 12345

requested_file_name = "example.txt"

start_file_client(file_server_host, file_server_port, requested_file_name)
