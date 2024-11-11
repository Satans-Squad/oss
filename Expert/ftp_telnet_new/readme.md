
# FTP and Telnet Server in Docker

This guide sets up a Docker container with FTP and Telnet services. It walks through building the Docker image, configuring services, and testing connections from the host machine.

## Steps

### 1. Build the Docker Image

```bash
docker build -t ftp-telnet-server .
```

### 2. Ensure Ports are Free

Check if ports 21 and 23 are free:

```bash
sudo lsof -i :<port-no>
```

(Optional) If ports are occupied, free them:

```bash
sudo kill -9 <process-id>
```

### 3. Run the Docker Container

Run the container and map ports for FTP and Telnet:

```bash
docker run -d -p 20-21:20-21 -p 23:23 -p 40000-40100:40000-40100 --name ftp-telnet ftp-telnet-server
```

## FTP Setup

1. **Connect to FTP**:
   ```bash
   ftp localhost
   ```

2. **Login with anonymous user**:
   - **Username**: `anonymous`
   - **Password**: *(Press Enter)*

3. **Access the Server**: You should now have access to the FTP server.

## Telnet Setup on Ubuntu Container

1. **Run a new container for Telnet setup**:
   ```bash
   docker run --privileged -ti ubuntu:20.04 bash
   ```

2. **Update Packages and Install Telnet**:
   ```bash
   apt update
   apt install telnetd xinetd nano -y
   ```

3. **Configure Telnet**:
   - Open configuration file:
     ```bash
     nano /etc/xinetd.d/telnet
     ```
   - Add the following configuration:
     ```plaintext
     service telnet
     {
       flags = REUSE
       socket_type = stream
       wait = no
       user = root
       server = /usr/sbin/in.telnetd
       log_on_failure += USERID
       disable = no
     }
     ```

4. **Add a New User for Telnet Access**:
   ```bash
   adduser newuser
   passwd newuser
   ```

5. **Start xinetd Service**:
   ```bash
   service xinetd restart
   ```

6. **Get the Container's IP Address**:
   - Install network tools:
     ```bash
     apt install net-tools -y
     ```
   - Find the IP address:
     ```bash
     ifconfig
     ```
   - Note the IP address, typically in the `172.17.x.x` range.

7. **Access Telnet from Another Machine**:
   ```bash
   telnet <container-ip>
   ```

   - Use the new user credentials to log in and access remote login.