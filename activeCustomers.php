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
	//read in the most active customers from multiple tables
	$query="select Fname, Lname, email from customer where customerID in (select customerID from orders where (select DATEDIFF(CURDATE(), date) < 30)group by customerID having count(*) > 1)";	
	$result = mysql_query($query);
	
	echo "<p>";
	echo "Active Customers <br> <br>";
	while($row = mysql_fetch_array($result))
	{
		$first= $row["Fname"];
                $last= $row["Lname"];
		$email= $row["email"];

                echo "$first $last <br>";
		echo "E-mail: $email <br> <br>"; 
	}

	echo "</p>";
	
      	mysql_free_result($result);
	mysql_close();

?>

<?php
  include('footer.php');
?>

</body>

