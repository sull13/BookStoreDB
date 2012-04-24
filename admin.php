<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
 "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <title>FancyBooks4Cheap</title>
  <meta http-equiv="Content-Type"
        content="application/xhtml+xml; charset=UTF-8" />
  <link rel="stylesheet" type="text/css" href="style.css" title="Default
Style"/>

</head>

<body>
<?php
  include('header.php');
?>
  <!-- page content -->
  <p>Admin Page</p>
  <a href= "displayCustomer.cgi"> Display Customers</a> <br>
  <a href= "AddUpdateCustomer.php?type=add"> Add Customer</a> <br>
  <a href= "displayPublisher.cgi"> Display Publishers</a> <br>
  <a href= "AddUpdatePublisher.php?type=add">Add Publisher</a> <br>
  <a href= "searchBook.cgi?type=update">Display Books</a> <br>
  <a href= "AddUpdateBook.php?type=add">Add Book</a> <br>
  <a href= "stock.php">View Inventory</a> <br>
  <a href= "reorderBooks.php">Reorder Books</a> <br>
  <a href= "activeCustomers.php">Active Customers</a> <br>
  <a href= "inactiveCustomers.php">Inactive Customers</a> <br>
  <a href= "booksNotSelling.php"> Books Not Selling</a> 
<?php
  include('footer.php');
?>

</body>

