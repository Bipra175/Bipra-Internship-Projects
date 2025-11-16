<?php
include '../config.php';

if (isset($_GET['id'])) {
  $id = $_GET['id'];
  $result = $conn->query("SELECT * FROM contacts WHERE id=$id");
  $row = $result->fetch_assoc();
}

if (isset($_POST['update'])) {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $message = $_POST['message'];

  $conn->query("UPDATE contacts SET name='$name', email='$email', message='$message' WHERE id=$id");
  header("Location: index.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Edit Contact</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-5">
  <div class="container">
    <h2>Edit Contact</h2>
    <form method="POST">
      <div class="mb-3">
        <label>Name:</label>
        <input type="text" name="name" class="form-control" value="<?= $row['name'] ?>" required>
      </div>
      <div class="mb-3">
        <label>Email:</label>
        <input type="email" name="email" class="form-control" value="<?= $row['email'] ?>" required>
      </div>
      <div class="mb-3">
        <label>Message:</label>
        <textarea name="message" class="form-control" required><?= $row['message'] ?></textarea>
      </div>
      <button type="submit" name="update" class="btn btn-primary">Update</button>
      <a href="index.php" class="btn btn-secondary">Cancel</a>
    </form>
  </div>
</body>
</html>
