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
	//connect to the database to obtain the given customers orders
	mysql_connect("localhost:/tmp/mysql-51.sock", "sulliv49", "redcreed2") 
	or die("Could not connect: " . mysql_error());
       	mysql_select_db("sulliv49");

	//read in all the results needed within multiple tables
	//first use the customer id to obtain data from the orders table
	$query="SELECT OID,date,customerID FROM orders WHERE customerID='0001'";	
	$result = mysql_query($query);
	echo "<p>";
	while($row = mysql_fetch_array($result))
	{
		$OID= $row["OID"];
                $date= $row["date"];
                $custID= $row["customerID"];
		
		//use the current OID to determine which book was ordered
		//and how many of the given book was ordered
		$query2="SELECT ISBN,quantity from contain where OID= '$OID'";
		$result2 = mysql_query($query2);
		$row2= mysql_fetch_array($result2,MYSQL_ASSOC);
		$isbn= $row2["ISBN"];
		$quan= $row2["quantity"];
		mysql_free_result($result2);
		//use the isbn to get the title of the book
		//from the book table
		$query3="SELECT title from book where ISBN = '$isbn'";
		$result3= mysql_query($query3);
		$row3= mysql_fetch_array($result3,MYSQL_ASSOC);
		$title= $row3["title"];		
		mysql_free_result($result3);

                echo "Title: $title <br> ISBN: $isbn <br> Date Ordered: $date <br>";
                echo "Quantity Ordered: $quan <br>";
		echo "<a href='OrderStatus.cgi?OID=$OID'>Check Status</a> <br> <br>";
	}
	echo "</p>";
	
        mysql_free_result($result);
	mysql_close();
 
?>

<?php
  include('footer.php');
?>

</body>

