# Step 1
sudo apt update
sudo apt install vsftpd


# Step 2 configuration file

sudo nano /etc/vsftpd.conf


# Add the content in that file

listen=YES
listen_ipv6=NO
anonymous_enable=YES
write_enable=YES
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES


# creation of Pub Directory

sudo mkdir -p /srv/ftp/Pub
sudo chmod 777 /srv/ftp/Pub

sudo chown -R ftp:ftp /srv/ftp/Pub
sudo chmod -R 775 /srv/ftp/Pub


# Firewall config
sudo ufw status
sudo ufw allow 21/tcp
sudo ufw allow 1024:1048/tcp
sudo ufw reload
sudo ufw allow 10000:10100/tcp



# Restart 
sudo systemctl restart vsftpd

# Ensure the status is active

sudo systemctl status vsftpd