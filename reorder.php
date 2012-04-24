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

<?php
	//get the infomation passed in from searchBook.cgi
	//if we came from there
	$isbn= "";
	$isbn= $_GET["isbn"];
	$title= "";
	$title= $_GET["title"];
?>

  <!-- page content -->
  <p>Admin Reorder: <br> <?php printf("Title: $title"); ?> </p>

<form VALUE ="Order" action="reorder.cgi" method="post">
ISBN&nbsp&nbsp&nbsp<input type="text" name= "ISBN" value="<?php 
printf($isbn); ?>"  /> <br>
Quantity: <input type="text" name= "quan" /> <br>
Reorder Book<input type="submit" /> <br>
</form>

<?php
  include('footer.php');
?>

</body>

