#!/bin/bash

# Get container IP
CONTAINER_IP=$(hostname -i)

# Update passive address in vsftpd config
sed -i "s/pasv_address=.*/pasv_address=$CONTAINER_IP/" /etc/vsftpd.conf

# Ensure correct permissions for telnet
chmod 777 /dev/pts/
chmod 777 /dev/ptmx

# Stop services if already running
service xinetd stop

# Start services
service xinetd start
/usr/sbin/vsftpd /etc/vsftpd.conf &

# Display service status
echo "Checking service status..."
netstat -tulpn

# Keep container running
tail -f /dev/null