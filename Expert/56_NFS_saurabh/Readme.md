# NFS Docker using 2 Containers

# Stop all containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -aq)

# create directory
mkdir shared_directory

# give permissions
chmod 777 shared_directory

# Build compose

docker-compose up -d

# Open two Terminals side by side

# Terminal 1

docker exec nfs-server bash -c "echo 'test' > /shared_directory/test.txt"
<!-- docker exec -it nfs-server bash -->

# check if shared_directory is present 
ls

# go to shared_directory

cd shared_directory



# Terminal 2

docker exec -it nfs-client bash

# check if shared_directory is present 

ls

# go to shared_directory

cd local_shared_directory


# Now create files in either Client or Server and wiill reflect the files on both sides