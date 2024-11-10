FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    vsftpd \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Create FTP directory structure with proper permissions
RUN mkdir -p /var/ftp/pub && \
    chmod 555 /var/ftp && \
    chmod 555 /var/ftp/pub && \
    chown -R root:root /var/ftp

# Add test files
RUN echo "Test file 1" > /var/ftp/pub/test1.txt && \
    echo "Test file 2" > /var/ftp/pub/test2.txt && \
    chmod 444 /var/ftp/pub/*.txt && \
    chown root:root /var/ftp/pub/*.txt

# Configure vsftpd
COPY vsftpd.conf /etc/vsftpd.conf

# Copy and set up start script
COPY start-services.sh /start-services.sh
RUN chmod +x /start-services.sh

EXPOSE 20 21 50000-50010

CMD ["/start-services.sh"]