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
	//connect to the database to obtain the suggested books
	mysql_connect("localhost:/tmp/mysql-51.sock", "sulliv49", "redcreed2") 
	or die("Could not connect: " . mysql_error());
       	mysql_select_db("sulliv49");
	//read in all the results needed within multiple tables
	//first use the customer id to obtain data from the orders table
	$query="select * from book where ISBN not in (	select ISBN from contain where OID in (	select OID from orders where (select DATEDIFF(CURDATE(), date) <  30)));";	
	$result = mysql_query($query);
	
	echo "<p>";

	echo "Books that have not sold in the last 30 days. <br> <br>";

	while($row = mysql_fetch_array($result))
	{
		$isbn= $row["ISBN"];
                $title= $row["title"];
                $subject= $row["author"];
		$price= $row["price"];
		$publisher= $row["publisher_name"];

                echo "ISBN: $isbn <br> Title: $title <br>"; 
 		echo "Author: $author <br> Price: $price";
                echo "<br> Publisher: $publisher <br>";
		echo "<br>";
	}

	echo "</p>";
	
      	mysql_free_result($result);
	mysql_close();

?>

<?php
  include('footer.php');
?>

</body>

