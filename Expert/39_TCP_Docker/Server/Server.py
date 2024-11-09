#server/server.py
import socket


HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345      # Port to listen on


def start_server():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.bind((HOST, PORT))
       s.listen()
       print(f"Server listening on {HOST}:{PORT}...")


       conn, addr = s.accept()
       with conn:
           print(f"Connected by {addr}")
           while True:
               data = conn.recv(1024)
               if not data:
                   break
               print(f"Received from client: {data.decode()}")
               conn.sendall(b"Hello from Server!")


if __name__ == "__main__":
   start_server()






'''
Steps:-
# Create Network
docker network create tcp_network

# Build server image
docker build -t server_image ./Server

# Build client image
docker build -t client_image ./Client


#After Image is created

# Start the server container
docker run -d --name server_container --network tcp_network server_image

# Start the client container
docker run --name client_container --network tcp_network client_image


# Check server logs
docker logs server_container

# Check client logs
docker logs client_container




'''