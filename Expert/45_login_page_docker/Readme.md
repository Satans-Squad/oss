# Optional starts

docker ps

# Stop all containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -aq)


# Optional ends


# Follow the Steps

# Build Dockerfile
docker build -t login-web-app .

# Run Container
docker run -d -p 80:80 --name login-web-container login-web-app

# Go to
http://localhost