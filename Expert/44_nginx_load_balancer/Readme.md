# Step 1

docker run -d --name wordpress-db \
  -e MYSQL_ROOT_PASSWORD=root_password \
  -e MYSQL_DATABASE=wordpress \
  -p 3307:3306 mysql:5.7

# Step 2

docker run -d --name wordpress \
  --link wordpress-db:mysql \
  -p 8080:80 \
  -e WORDPRESS_DB_HOST=wordpress-db:3306 \
  -e WORDPRESS_DB_NAME=wordpress \
  -e WORDPRESS_DB_USER=root \
  -e WORDPRESS_DB_PASSWORD=root_password \
  wordpress:latest

# Step 3 - Go and ensure http://localhost:8080 is running

# Step 4 - Run Nginx

docker run -d --name nginx \
  -p 80:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
  --link wordpress:wordpress \
  nginx:latest


# For Logs
docker logs wordpress
docker logs nginx
docker logs wordpress-db
