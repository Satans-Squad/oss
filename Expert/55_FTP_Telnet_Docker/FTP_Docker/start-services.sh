#!/bin/bash

# Get container IP
CONTAINER_IP=$(hostname -i)

# Update passive address in vsftpd config
sed -i "s/pasv_address=.*/pasv_address=$CONTAINER_IP/" /etc/vsftpd.conf

# Start vsftpd in foreground mode
/usr/sbin/vsftpd /etc/vsftpd.conf