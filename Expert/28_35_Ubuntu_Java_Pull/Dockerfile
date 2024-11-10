# Use the official OpenJDK Alpine image (latest version)
FROM openjdk:alpine

# Set the working directory
WORKDIR /app

# Copy your Java application code (update with your actual file)
COPY HelloWorld.java .

# Compile the Java application
RUN javac HelloWorld.java

# Specify the command to run the application
CMD ["java", "HelloWorld"]


# docker build -t hello-world-java .
# docker run --rm hello-world-java
