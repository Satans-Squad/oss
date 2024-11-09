# Step 1

docker-compose up -d

# Step 2

http://localhost:8989/admin/install.php

# Step 3 Installation

Configure the database settings
On the installation page, you'll need to enter the database details:

# Type of Database: MySQL/MySQLi
# Hostname (for Database Server): mysql (this is the service name in your docker-compose.yml file)
# Username (for Database): mantisbt
# Password (for Database): mantisbt
# Database name (for Database): bugtracker
# Admin Username (to create Database if required): root
# Admin Password (to create Database if required): root
# Leave the "Print SQL Queries" option unchecked unless you want to see the SQL queries being generated.

# Click Install/Upgrade Database.



# STEP 4

Head to

# http://localhost:8989

You will see Login Page
Username: administrator
Password: root