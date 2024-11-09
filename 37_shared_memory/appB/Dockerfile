# Use a base image with build tools
FROM gcc:latest

# Set the working directory
WORKDIR /app

# Copy the C source file
COPY shared_memory_reader.c .

# Compile the C application
RUN gcc -o reader shared_memory_reader.c -lrt

# Command to run the application
CMD ["./reader"]


# Build Image
# docker build -t appone .

# After Building the Docker image do this
# docker volume create shm_volume

# # Run App A
# docker run --rm --mount source=shm_volume,target=/dev/shm app-a

# # Run App B (this should be in another terminal)
# docker run --rm --mount source=shm_volume,target=/dev/shm app-b
