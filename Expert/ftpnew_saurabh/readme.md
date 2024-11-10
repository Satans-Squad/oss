# Build the Docker image with the Dockerfile
docker build -t ftp-server .

# Run the container with port mapping to allow FTP traffic from the host
docker run -d --name my-ftp-server -p 21:21 -p 1024-1048:1024-1048 -p 10000-10100:10000-10100 ftp-server

# on client side: now open new terminal on your local machine and connect with ftp server
1. ftp localhost 21
2. enter uname as "anonymous"
3. skip the password
4. ls
4. you can see "Pub" dir
5. you can create file in Pub dir

# on server side:
1. docker exec -it <container-id> bash
2. cd srv/ftp/Pub
3. you can see your changes




