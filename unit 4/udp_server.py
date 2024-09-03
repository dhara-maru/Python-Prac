import socket

def start_udp_server(host, port):
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    while True:
      
        data, client_address = server_socket.recvfrom(1024)

  
        response_message = "Hello, client! This is the UDP server."
        server_socket.sendto(response_message.encode('utf-8'), client_address)
        print(f"Response sent to {client_address}")

udp_server_host = "127.0.0.1"  
udp_server_port = 54321

start_udp_server(udp_server_host, udp_server_port)
