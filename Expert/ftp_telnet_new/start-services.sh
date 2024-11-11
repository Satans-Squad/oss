#!/bin/bash
# Start xinetd (for telnet)
/usr/sbin/xinetd -dontfork &
# Start vsftpd
/usr/sbin/vsftpd /etc/vsftpd.conf &
# Keep container running
tail -f /dev/null