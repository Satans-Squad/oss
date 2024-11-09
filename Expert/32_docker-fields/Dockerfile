# Use the official Ubuntu image as the base
FROM ubuntu:latest

# Install Nginx and any necessary dependencies
RUN apt-get update && apt-get install -y nginx && apt-get clean

# Expose port 80 to the host
EXPOSE 80

# Start Nginx in the foreground so the container keeps running
CMD ["nginx", "-g", "daemon off;"]
