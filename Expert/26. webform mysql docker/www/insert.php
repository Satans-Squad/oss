<?php
$servername = "mysql";  // Use the MySQL service name defined in docker-compose.yml
$username = "root";  // MySQL root username
$password = "rootpassword";  // MySQL root password
$dbname = "webform_db";  // Your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get data from the form
$name = $_POST['name'];
$email = $_POST['email'];

// Prepare and bind SQL query to prevent SQL injection
$stmt = $conn->prepare("INSERT INTO records (name, email) VALUES (?, ?)");
$stmt->bind_param("ss", $name, $email);

// Execute the statement
if ($stmt->execute()) {
    echo "New record inserted successfully!";
} else {
    echo "Error: " . $stmt->error;
}

// Close the connection
$stmt->close();
$conn->close();
?>
