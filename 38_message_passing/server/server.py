import socket

# Server settings
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345       # Port to bind to

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

# Accept client connection
conn, addr = server_socket.accept()
print(f"Connection from {addr}")

# Receive message from client
data = conn.recv(1024)
print(f"Received from client: {data.decode()}")

# Send response to client
conn.sendall(b"Hello from the server!")

# Close connection
conn.close()
