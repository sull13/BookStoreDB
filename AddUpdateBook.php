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
	
	//Check if we are adding a new customer or updating
	//an already existing customer
	$type = "";
	$type = $_GET["type"];
	$CID = "";
	$ISBN = $_GET["ISBN"];

	//check if we are updating the database and the isbn
	//was given through the link, meaning modify in the book
	//list was clicked on
	if( ($type === "update") && (!($ISBN === "")) && (!(is_null($ISBN) )) ) 
	{
		mysql_connect("localhost:/tmp/mysql-51.sock", "sulliv49", "redcreed2") or
                        die("Could not connect: " . mysql_error());
                mysql_select_db("sulliv49");
	
                $result = mysql_query("SELECT * FROM book WHERE ISBN='$ISBN'");

                $row = mysql_fetch_array($result, MYSQL_ASSOC);
                $isbn = $row["ISBN"];
                $title = $row["title"];
                $subject = $row["subject"];
                $author = $row["author"];
                $price = $row["price"];
		$stock = $row["stock"];
                $publisher_name = $row["publisher_name"];
                mysql_free_result($result);

	} 
?>

 
  
<!-- page content -->
<?php
if($type === "update") 
{
	printf("<p> Update Book</p>");
}
else
{
	printf("<p> Add Book</p>");
}
?>


  <form action="AddUpdateBook.cgi" method="post">
<?php if($type === 'add'){printf("ISBN:");} ?> 
<input type="<?php if($type === 'update'){printf("hidden");}else{printf("text");} ?>" name = "ISBN" value="<?php 
printf($isbn); ?>" /><br>
Title: <input type="text" name = "Title" value="<?php printf($title); ?>" 
/><br>
Subject: <input type="text" name = "Subject" value="<?php 
printf($subject); ?>"  
/><br>
Author: <input type="text" name = "Author" value="<?php printf($author); 
?>" /> 
<br>
Price: <input type="text" name = "Price" value="<?php printf($price); ?>" 
/><br>
Stock: <input type="text" name = "Stock" value="<?php printf($stock); ?>"
/><br>
Publisher Name: <input type="text" name = "pname" value="<?php 
printf($publisher_name); ?>" /><br>

<input type="hidden" name= type value="<?php printf($type); ?>" /> 

Update/Add Book<input type="submit" /> <br>
</form>

<?php
  include('footer.php');
?>

</body>

