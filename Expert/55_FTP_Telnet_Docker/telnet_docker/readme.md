docker build -t telnet-server .

docker run -d -p 23:23 --name telnet-container telnet-server

telnet localhost