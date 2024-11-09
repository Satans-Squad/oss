# Use a base image with build tools
FROM gcc:latest

# Set the working directory
WORKDIR /app

# Copy the C source file
COPY shared_memory_writer.c .

# Compile the C application
RUN gcc -o writer shared_memory_writer.c -lrt

# Command to run the application
CMD ["./writer"]
