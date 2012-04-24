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
                $fname = $row["Fname"];
                $lname = $row["Lname"];
                $street = $row["street"];
                $city = $row["city"];
                $zip = $row["zip"];
                $email = $row["email"];
		$phone = $row["phone"];
                mysql_free_result($result);

	} 
?>

 
  
<!-- page content -->
<?php
if($type === "update") 
{
	printf("<p> Update Customer</p>");
}
else
{
	printf("<p> Add Customer</p>");
}
?>


  <form action="AddUpdateCustomer.cgi" method="post">
<?php if($type === 'add'){printf("Customer ID:");} ?> 
<input type="<?php if($type === 'update'){printf("hidden");}else{printf("text");} ?>
" name="cid" value="<?php printf($CID); ?>" /> <br>
First Name:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="fname" value="<?php printf($fname); ?>" /> <br>
Last Name:&nbsp&nbsp&nbsp<input type="text" name= "lname" value="<?php printf($lname); ?>" /> <br>
Street: <input type="text" name= "street" value="<?php printf($street); ?>" /> <br>
City: <input type="text" name= "city" value="<?php printf($city); ?>"  /> <br>
Zip: <input type="text" name= "zip" value="<?php printf($zip); ?>" /> <br>
E-mail: <input type="text" name= "email" value="<?php printf($email); ?>" /> <br>
Phone: <input type="text" name= "phone" value="<?php printf($phone); ?>" /> <br>
       <input type="hidden" name= type value="<?php printf($type); ?>" /> 

Update/Add Customer<input type="submit" /> <br>
</form>

<?php
  include('footer.php');
?>

</body>

