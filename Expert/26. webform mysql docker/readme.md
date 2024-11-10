# Build and start the containers
docker-compose up -d

# To ensure both containers are running
docker ps

You should see both `mysql_db` and `php_web` containers running.


### 5. **Set up MySQL Database:**

You'll need to set up the database table in MySQL.

#### 5.1 **Connect to the MySQL container:**

```bash
docker exec -it mysql_db bash
```

# Once inside the MySQL container, log into MySQL:

```bash
mysql -u root -p
```
# Enter the password = rootpassword


#### 5.2 **Create the database and table:**

```sql
USE webform_db;

CREATE TABLE records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```

### 6. **Access the Web Form:**

Now, open your browser and go to `http://localhost:8080`. You should see the HTML form where you can enter a name and email to insert into the MySQL database.

### 7. **Test the Form:**

1. Enter a name and email in the form and submit.
2. You should see a success message like "New record inserted successfully!".
3. You can verify the data in MySQL by logging into the MySQL container and running:

   ```sql
   USE webform_db;
   SELECT * FROM records;
   ```