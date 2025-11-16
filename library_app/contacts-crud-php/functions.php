<?php
// This is the function to connect to the database
function getConnection() {
    $conn = new mysqli("localhost", "root", "", "contacts_app");
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// The given function code is used to get all contacts
function getContacts() {
    $conn = getConnection();
    $result = $conn->query("SELECT * FROM contacts ORDER BY id DESC");
    $contacts = [];
    while ($row = $result->fetch_assoc()) {
        $contacts[] = $row;
    }
    $conn->close();
    return $contacts;
}
?>
