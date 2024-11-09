
sudo apt-get install docker-compose


folder structure be like

docker-socket-communication/
├── server/
│ ├── Dockerfile
│ ├── server.py
├── client/
│ ├── Dockerfile
│ ├── client.py
├── docker-compose.yml



Open a terminal in the `docker-socket-communication` directory and run the following commands:


1. Build the Docker images

docker-compose build



2. Run the containers:

docker-compose up


