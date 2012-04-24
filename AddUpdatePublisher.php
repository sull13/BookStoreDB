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
	$CID = $_GET["CID"];

	//check if we are updating the database and the customer id
	//was given through the link, meaning modify in the customer
	//list was clicked on
	if( ($type === "update") && (!($CID === "")) && (!(is_null($CID) )) ) 
	{
		mysql_connect("localhost:/tmp/mysql-51.sock", "sulliv49", "redcreed2") or
                        die("Could not connect: " . mysql_error());
                mysql_select_db("sulliv49");
	
                $result = mysql_query("SELECT * FROM customer WHERE customerID='$CID'");

                $row = mysql_fetch_array($result, MYSQL_ASSOC);
                $name = $row["publisher_name"];
                
                
                $city = $row["city"];
              
              
                mysql_free_result($result);

	} 
?>

 
  
<!-- page content -->
<?php
if($type === "update") 
{
	printf("<p> Update Publisher</p>");
}
else
{
	printf("<p> Add Publisher</p>");
}
?>


  <form action="AddUpdatePublisher.cgi" method="post">
Publisher Name:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="Name" 
value="<?php printf($name); ?>" /> <br>
City: <input type="text" name= "city" value="<?php printf($city); ?>"  /> <br>
       <input type="hidden" name= type value="<?php printf($type); ?>" /> 

Update/Add Publisher<input type="submit" /> <br>
</form>

<?php
  include('footer.php');
?>

</body>

