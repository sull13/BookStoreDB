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
  <p>Advanced Search.</p>

  <form action="searchBook.cgi" method="post">
Author: <input type="text" name="Author" /> <br>
Title:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="Title" /> <br>
ISBN&nbsp&nbsp&nbsp<input type="text" name= "ISBN" /> <br>
Subject <input type="text" name= "sub" /> <br>
Publisher <input type="text" name= "pub" /> <br>
Find Book<input type="submit" /> <br>
</form>

<?php
  include('footer.php');
?>

</body>



