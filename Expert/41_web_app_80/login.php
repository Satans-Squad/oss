<?php
// Enable error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection parameters
$host = getenv('DB_HOST') ?: 'mysql-db';
$dbname = getenv('DB_NAME') ?: 'logindb';
$username = getenv('DB_USER') ?: 'root';
$password = getenv('DB_PASSWORD') ?: 'rootpassword';

try {
    // Create database connection
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Check if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Get form data
        $username = isset($_POST['username']) ? trim($_POST['username']) : '';
        $password = isset($_POST['password']) ? trim($_POST['password']) : '';
        
        if (empty($username) || empty($password)) {
            echo "Please fill in all fields";
            exit;
        }
        
        // Prepare and execute query
        $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
        $stmt->execute([$username, $password]);
        
        if ($stmt->rowCount() > 0) {
            echo "<div style='color: green; padding: 20px;'>
                    Login successful!<br>
                    Connected to instance: " . gethostname() . "
                  </div>";
        } else {
            echo "<div style='color: red; padding: 20px;'>
                    Invalid credentials!<br>
                    Please try again.
                  </div>";
        }
    } else {
        echo "<div style='color: red; padding: 20px;'>
                No form data received. Please submit the form.
              </div>";
    }
} catch(PDOException $e) {
    echo "<div style='color: red; padding: 20px;'>
            Database Connection Error: " . $e->getMessage() . "
          </div>";
}
?>