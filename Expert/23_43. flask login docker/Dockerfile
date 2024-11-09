# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY app.py .
COPY templates /app/templates

# Install Flask
RUN pip install Flask

# Expose port 7000
EXPOSE 7000

# Run the application
CMD ["python", "app.py"]
