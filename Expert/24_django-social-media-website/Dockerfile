# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .


# Open port 8000 for Django development server
EXPOSE 8000

# Run database migrations and start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
