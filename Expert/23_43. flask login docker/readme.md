# build docker file
docker build -t flask-login-app .

# Run container
docker run -d -p 7000:7000 flask-login-app

# visit this url to see app
http://localhost:7000

Note: You should see the login form. When you submit a username and password, it will return a message indicating whether the login was successful or failed.
