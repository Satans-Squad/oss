# Step 1
docker-compose up -d

# Step 2 - Wait for some time to start nginx and go to http://localhost:8081

# Step 3 -  docker exec -it ubuntu-demo bash

Now perform all commands of docker and write theory for all field of docker compose 


To demonstrate the creation of containers from a particular Linux distribution (distro) and show the Docker Compose file fields, we'll create an example using Ubuntu as the base image and explain the Docker Compose fields.

Step 1: Create a Docker Compose Project Directory
Start by creating a project directory and navigating into it:

bash
Copy code
mkdir ubuntu-docker-compose && cd ubuntu-docker-compose
Step 2: Create the docker-compose.yml File
The docker-compose.yml file defines how to configure and manage Docker containers. Here’s an example using the Ubuntu image for the container, which could be used to run a simple command like a bash shell.

Example docker-compose.yml for Ubuntu:
yaml
Copy code
version: '3.8'

services:
  ubuntu-container:
    image: ubuntu:latest         # Use the official Ubuntu image
    container_name: ubuntu-demo  # Name of the container
    command: ["bash"]           # Run a bash shell
    ports:
      - "8080:80"               # Map port 80 in the container to port 8080 on the host
    volumes:
      - ./my-data:/data         # Mount ./my-data on the host to /data in the container
    environment:
      - MY_ENV_VAR=example      # Set an environment variable inside the container
    networks:
      - my-network              # Attach the container to a custom network
    restart: always             # Always restart the container if it stops
    depends_on:
      - another-service         # If another service is required (optional)

networks:
  my-network:
    driver: bridge              # Specify the network driver to use
Explanation of Docker Compose Fields:
version: Specifies the version of Docker Compose to use. In this example, it's set to 3.8, which is one of the latest stable versions.

services: Defines the containers (services) that will run as part of the application. In this case, we are creating an ubuntu-container service.

image: The Docker image to use for the container. Here, ubuntu:latest is used.
container_name: Specifies the name of the container. It’s helpful for easy identification.
command: The command that runs when the container starts. In this case, it will start a bash shell.
ports: A list of port mappings. In this case, it maps port 8080 on the host to port 80 inside the container.
volumes: Binds a local directory (./my-data) to a directory inside the container (/data). This allows data persistence.
environment: Environment variables that are set inside the container.
networks: Defines which network the container will connect to. Here, the container is attached to a custom network called my-network.
restart: Determines when the container should restart. always will restart the container if it stops unexpectedly.
depends_on: Lists any other services that should be started before this service. This is used if one container depends on the other.
networks: This section defines the custom network (my-network) to be used by the container. The bridge driver is used, which is the default Docker networking driver.

Step 3: Running Docker Compose
After you've created the docker-compose.yml file, you can run the services by executing the following command:

bash
Copy code
docker-compose up -d
The -d flag runs the containers in detached mode (in the background).
Step 4: Interacting with the Ubuntu Container
You can check if the container is running by using the following command:

bash
Copy code
docker ps
You should see the ubuntu-demo container listed in the output.

To access the running container’s bash shell, use:

bash
Copy code
docker exec -it ubuntu-demo bash
Step 5: Stopping and Removing the Containers
To stop the containers:

bash
Copy code
docker-compose down
This will stop and remove the containers, networks, and volumes created by Docker Compose.

Summary of Docker Compose File Fields:
Here’s a list of the key fields in the Docker Compose file:

version: Version of Docker Compose syntax.
services:
image: Docker image to use for the container.
container_name: Name of the container.
command: Command to run when the container starts.
ports: Port mappings between the host and container.
volumes: Volume mappings for persistent storage.
environment: Environment variables for the container.
networks: Networks that the container should connect to.
restart: Policy for restarting the container if it stops.
depends_on: Dependencies on other services.
networks: Custom networks configuration.