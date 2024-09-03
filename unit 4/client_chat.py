import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received: {message}")

    except:
        pass
    finally:
        client_socket.close()
        print("Connection closed.")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

# Start a thread to receive messages
threading.Thread(target=receive_messages, args=(client,)).start()

try:
    while True:
        message = input("Your message: ")
        client.sendall(message.encode('utf-8'))

except KeyboardInterrupt:
    client.close()
    print("Client terminated.")
