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
	//connect to the database to obtain the books that have to be reordered
	mysql_connect("localhost:/tmp/mysql-51.sock", "sulliv49", "redcreed2") 
	or die("Could not connect: " . mysql_error());
       	mysql_select_db("sulliv49");
	//select the books from the book table that have less than 6 books left in stock
	$query="SELECT * from book where stock <= 5";	
	$result = mysql_query($query);
	
	echo "<p>";
	echo "Books that are low in stock <br> <br>";	
	while($row = mysql_fetch_array($result))
	{
		$isbn= $row["ISBN"];
                $title= $row["title"];
                $author= $row["author"];
		$price= $row["price"];
		$publisher= $row["publisher_name"];
		$stock= $row["stock"];
	
                echo "ISBN: $isbn <br> Title: $title <br>"; 
 		echo "Author: $author <br> Price: $price";
                echo "<br> Publisher: $publisher <br>";
		echo "Stock Remaining: $stock <br>";
		echo "<a href='reorder.php?isbn=$isbn&title=$title'>Reorder Book</a> <br> <br>";	
	}
	
	echo "</p>";
      	mysql_free_result($result);
	mysql_close();

?>

<?php
  include('footer.php');
?>

</body>

