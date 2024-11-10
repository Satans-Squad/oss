# Dockerfile
FROM alpine:latest

# Install busybox-extras which includes telnetd
RUN apk add --no-cache busybox-extras

# Create a test user
RUN adduser -D telnetuser && \
    echo "telnetuser:password" | chpasswd

# Expose telnet port
EXPOSE 23

# Start telnetd in foreground mode
CMD ["/usr/sbin/telnetd", "-F", "-l", "/bin/sh"]