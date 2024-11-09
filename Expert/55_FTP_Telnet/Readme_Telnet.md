# Step 1

sudo apt update
sudo apt install telnet
sudo apt install xinetd telnetd -y


# Step 2

sudo nano /etc/xinetd.d/telnet

# Step 3

service telnet
{
    disable = no
    flags = REUSE
    socket_type = stream
    wait = no
    user = root
    server = /usr/sbin/in.telnetd
    log_on_failure += USERID
    only_from = 0.0.0.0   # Allows access from any IP
}

Save this in that file

# Step 4- Close the file and

sudo service xinetd restart


# Step 5
sudo systemctl enable xinetd

# Step 6 Allow Firewall
sudo ufw allow 23/tcp


# Step 7
To access telnet

telnet <ip-address>