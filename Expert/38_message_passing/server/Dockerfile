# Use Python official image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the server code
COPY server.py .

# Expose the port
EXPOSE 12345

# Run the server script
CMD ["python", "server.py"]
