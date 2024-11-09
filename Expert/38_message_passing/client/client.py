import socket

# Client settings
HOST = 'server'  # Server container name, will be linked via Docker network
PORT = 12345     # Port to connect to

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send message to server
client_socket.sendall(b"Hello from the client!")

# Receive response from server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Close connection
client_socket.close()
