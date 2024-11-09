# Dockerfile
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    vsftpd \
    telnetd \
    xinetd \
    net-tools \
    inetutils-telnetd \  # Add this package
    && rm -rf /var/lib/apt/lists/*

# Create necessary directories
RUN mkdir -p /var/ftp/pub && \
    chmod 555 /var/ftp && \
    chmod 777 /var/ftp/pub && \
    chown nobody:nogroup /var/ftp/pub

# Configure vsftpd
COPY vsftpd.conf /etc/vsftpd.conf

# Configure telnet
COPY telnet /etc/xinetd.d/telnet

# Start services script
COPY start-services.sh /start-services.sh
RUN chmod +x /start-services.sh

EXPOSE 20 21 23 40000-40100

CMD ["/start-services.sh"]