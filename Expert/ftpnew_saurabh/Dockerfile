# Dockerfile

FROM ubuntu:latest

# Install vsftpd
RUN apt update && apt install -y vsftpd

# Copy vsftpd configuration file
COPY vsftpd.conf /etc/vsftpd.conf

# Create FTP directory
RUN mkdir -p /srv/ftp/Pub && chmod 777 /srv/ftp/Pub

# Expose FTP ports
EXPOSE 21 1024-1048 10000-10100

# Start vsftpd
CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]
