# Build the server image
docker build -t app_server ./server

# Build the client image
docker build -t app_client ./client

# Create Network
docker network create app-network

# Run Server
docker run -d --name server --network app-network app_server

# Run Client
docker run --rm --network app-network app_client
