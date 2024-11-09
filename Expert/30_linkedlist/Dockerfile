# Use an official GCC image as the base
FROM gcc:latest

# Copy the C program to the container
COPY linked_list.c /usr/src/linked_list.c

# Set the working directory
WORKDIR /usr/src

# Compile the C program
RUN gcc -o linked_list linked_list.c

# Run the executable by default when the container starts
CMD ["./linked_list"]
