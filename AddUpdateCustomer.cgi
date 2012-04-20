#!/opt/csw/bin/perl

use CGI::Carp qw(fatalsToBrowser);
use warnings;
#use CGI ':standard';
use strict;
use CGI qw/:standard :html3/;
use DBI;
#use POSIX qw(strftime);
#use Class::Struct;
print "Content-type: text/html\n\n";

#definition of variables needed
my($type,$custID,$fname,$lname,$street,$city,$zip,$email,$phone);
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;
$type= $obj->param("type");
$custID= $obj->param("cid");
$fname= $obj->param("fname");
$lname= $obj->param("lname");
$street= $obj->param("street");
$city= $obj->param("city");
$zip= $obj->param("zip");
$email= $obj->param("email");
$phone= $obj->param("phone");

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to
database:$DBI::errstr\n";

#check that the cust ID has not been used already
#since is it the primary key
my $sql = "SELECT customerID from customer where customerID = '$custID'";
my $sth= $dbh->prepare($sql);
my $rows= $sth->execute();

if($type eq "add")
{
	if($rows > 0)
	{
		print "Customer ID is already in use. Try again.\n"
	}
	else
	{
		$sql = "INSERT INTO customer VALUES('$custID','$fname','$lname','$street','$city','$zip','$email','$phone');";
		print "New Customer has been added to the database.\n"
	}
} 
elsif($type eq "update")
{

		$sql = "UPDATE customer SET Fname = '$fname', Lname = '$lname', street = '$street', " .
		      "city = '$city', zip = '$zip', email = '$email', phone = '$phone' WHERE customerID = '$custID';";
		print "Customer information has been updated.\n";
}
else
{
	print "Invalid type- $type, should not get here.\n";

}

if($type eq "add" || $type eq "update")
{
	$sth= $dbh->prepare($sql);
	$sth->execute();
} 

$sth->finish();
