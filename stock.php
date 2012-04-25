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
	//select the books from the book table that have at least 1 book left in stock
	$query="SELECT ISBN,title,stock from book where stock >= 1";	
	$result = mysql_query($query);
	
	echo "<p>";


	echo "<table border='1'>
	      <tr>
	      <th>ISBN</th>
	      <th>Title</th>
	      <th>Stock</th>
	      <th></th>
	      </tr>";
	
	while($row = mysql_fetch_array($result))
	{
		$isbn= $row["ISBN"];
                $title= $row["title"];
		$stock= $row["stock"];
	
                /*echo "ISBN: $isbn <br> Title: $title <br>"; 
		echo "Stock: $stock <br>";
		echo "<a href='reorder.php?isbn=$isbn&title=$title'>Reorder Book</a> <br> <br>";	
		*/
		
		  echo "<tr><td>$isbn</td><td>$title</td><td>$stock</td><td><a href='reorder.php?isbn=$isbn&title=$title'>Reorder</a></td></tr>";

	}
	
	echo "</table></p>";
      	mysql_free_result($result);
	mysql_close();

?>

<?php
  include('footer.php');
?>

</body>

