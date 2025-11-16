<?php
include '../config.php'; // The file that connects PHP with the MySQL database

$message = ''; // The variable where message (success or error) will be stored

if (isset($_POST['submit'])) {
    // The values are taken from the form
    $name = $_POST['name'];
    $email = $_POST['email'];
    $msg = $_POST['message'];

    // The SQL query to add new contact into database
    $sql = "INSERT INTO contacts (name, email, message) VALUES ('$name', '$email', '$msg')";

    // The query runs and checks if it is successful or not
    if ($conn->query($sql)) {
        $message = "✅ Contact added successfully!";
    } else {
        $message = "❌ Error: " . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Contact</title>
    <!-- The Bootstrap link is added for better design and layout -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="p-5 bg-light">
    <div class="container">
        <h2 class="mb-4">Add New Contact</h2>

        <!-- The message will be shown here after adding contact -->
        <?php if ($message): ?>
            <div class="alert alert-info"><?= $message ?></div>
        <?php endif; ?>

        <!-- The form where user enters name, email and message -->
        <form method="POST">
            <div class="mb-3">
                <label class="form-label">Name</label>
                <input type="text" name="name" class="form-control" required>
            </div>

            <div class="mb-3">
                <label class="form-label">Email</label>
                <input type="email" name="email" class="form-control" required>
            </div>

            <div class="mb-3">
                <label class="form-label">Message</label>
                <textarea name="message" class="form-control" rows="4" required></textarea>
            </div>

            <!-- The button to add new contact and back to main page -->
            <button type="submit" name="submit" class="btn btn-primary">Add Contact</button>
            <a href="index.php" class="btn btn-secondary">Back</a>
        </form>
    </div>
</body>
</html>
