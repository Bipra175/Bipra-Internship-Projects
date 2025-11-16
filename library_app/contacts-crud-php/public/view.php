<?php
include 'functions.php';
$contacts = getContacts();
?>

<!DOCTYPE html>
<html>
<head>
  <title>View Contacts</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container mt-5">
    <h2 class="text-center mb-4">All Contacts</h2>
    <a href="add.php" class="btn btn-success mb-3">+ Add New</a>
    <table class="table table-bordered table-striped">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Message</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($contacts as $contact): ?>
        <tr>
          <td><?= $contact['id'] ?></td>
          <td><?= $contact['name'] ?></td>
          <td><?= $contact['email'] ?></td>
          <td><?= $contact['message'] ?></td>
          <td>
            <a href="edit.php?id=<?= $contact['id'] ?>" class="btn btn-sm btn-primary">Edit</a>
            <a href="delete.php?id=<?= $contact['id'] ?>" class="btn btn-sm btn-danger" onclick="return confirm('Delete this contact?')">Delete</a>
          </td>
        </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  </div>
</body>
</html>
