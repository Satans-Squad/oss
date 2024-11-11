FROM ubuntu:latest
# Install required packages
RUN apt-get update && apt-get install -y \
vsftpd \
telnetd \
xinetd \
&& rm -rf /var/lib/apt/lists/*
# Create necessary directories
RUN mkdir -p /var/ftp/pub && \
chmod 777 /var/ftp/pub && \
mkdir -p /var/run/vsftpd/empty
# Configure vsftpd
COPY vsftpd.conf /etc/vsftpd.conf
# Configure telnet
COPY telnet /etc/xinetd.d/telnet
# Create startup script
COPY start-services.sh /start-services.sh
RUN chmod +x /start-services.sh
# Expose ports
EXPOSE 20 21 23 40000-40100
# Start services
CMD ["/start-services.sh"]