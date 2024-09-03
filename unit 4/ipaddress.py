import socket

def get_ip_address():

        hostname = socket.gethostname()

        ip_address = socket.gethostbyname(hostname)
        
        return ip_address

ip_address = get_ip_address()
print(f"Your IP address is: {ip_address}")
