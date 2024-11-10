<?php
$servername = "db";  // Name of the MySQL container (use the MySQL container name here)
$username = "root";
$password = "password";  // Set the same password as in the container
$dbname = "my_database";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
