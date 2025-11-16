<?php
// Connecting the PHP with MySQL database

$servername = "localhost";
$username   = "root";
$password   = "";
$dbname     = "contacts_app";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
