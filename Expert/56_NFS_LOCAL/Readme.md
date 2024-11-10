# Installation

sudo apt install nfs-kernel-server
sudo apt install nfs-common


# Setting Up Server

cd Desktop
mkdir shared_directory

# setting path of shared_directory in exports file

pwd

NOTE: copy the output of pwd

sudo nano /etc/exports

# paste the path in exports file

/home/<username>/Desktop/shared_directory * (rw,sync,no_subtree_check)

# Save and exit the file using CTRL + S then CTRL + X

# Restart the server

sudo systemctl nfs-kernel-server

# Ensure the directory is shared using the following command

sudo exportfs -v

This command should show the directory you have created

# CLIENT CONFIGURATION

cd Documents
mkdir local_shared_directory

# Mounting the shared_directory to our local_shared_directory

sudo mount -t nfs 127.0.0.1:/home/<username>/Desktop/shared_directory ~/Documents/local_shared_directory

# Once done, create files in either folder which will reflect in other folder


