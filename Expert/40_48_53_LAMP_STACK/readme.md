# Optional starts

docker ps

# Stop all containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -aq)


# Optional ends


# Follow the steps

# Create Docker Network
docker network create lamp-network

# Build Dockerfile
docker build -t lampstack .

# Run MYSQL Container
docker run -d --name db --network lamp-network -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=my_database mysql:8.1.0


# Run both containers
docker run -d -p 80:80 --network lamp-network --name lamp-web lampstack


# Go to
http://localhost 

Connection Success message should be displayed