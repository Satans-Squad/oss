### Step 1: Build the Docker Image
```bash
docker build -t node-bind-mount-demo .
```

### Step 2: Run the Docker Container with Bind Mount
Use the following command to run the container with a bind mount. This will allow any changes made to `index.html` in your host system to reflect inside the container without needing to restart it.

```bash
docker run -p 3000:3000 -v "$(pwd)/index.html:/app/index.html" node-bind-mount-demo
```

With this setup:
- You can change the color in `index.html` on your local machine, and it will automatically reflect in the container.
- Access the application by navigating to `http://localhost:3000` in your browser.