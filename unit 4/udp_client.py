import socket

def start_udp_client(server_host, server_port):
   
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
      
        message = "Hello, UDP server! This is the client."
        client_socket.sendto(message.encode('utf-8'), (server_host, server_port))
        print(f"Message sent to UDP server at {server_host}:{server_port}")

        data, server_address = client_socket.recvfrom(1024)
        response_message = data.decode('utf-8')
        print(f"Received response from UDP server: {response_message}")

    finally:
     
        client_socket.close()
        print("UDP client socket closed.")

udp_server_host = "127.0.0.1"  
udp_server_port = 54321

start_udp_client(udp_server_host, udp_server_port)
