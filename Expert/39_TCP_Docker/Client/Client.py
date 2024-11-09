# client/client.py
import socket


SERVER_HOST = 'server'  # Hostname of the server as defined in docker-compose.yml
SERVER_PORT = 12345     # Port to connect to


def start_client():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.connect((SERVER_HOST, SERVER_PORT))
       print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")
       s.sendall(b"Hello from Client!")
       data = s.recv(1024)
       print(f"Received from server: {data.decode()}")


if __name__ == "__main__":
   start_client()
