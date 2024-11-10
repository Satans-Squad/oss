#Ensure your folder structure:

simple_web_app/
├── Dockerfile
├── index.html
└── nginx.conf

#Follow this steps:

1. build docker file
    docker build -t simple_web_app .

2. Run the container
    docker run -d -p 8080:80 simple_web_app

3. visit this site
    http://localhost:8080

