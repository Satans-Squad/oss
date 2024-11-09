# Step 1

docker build -t ubuntu-nginx-demo .

# Step 2
docker run -d -p 8081:80 --name ubuntu-nginx-container ubuntu-nginx-demo

change the port if conflict arrises

# Step 3
docker ps

# Step 4

http://localhost:8081
