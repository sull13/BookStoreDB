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
my($type,$isbn,$title,$subject,$author,$price,$stock,$publisherName);
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;
$type= $obj->param("type");
$isbn= $obj->param("ISBN");
$title=  $obj->param("Title");
$subject= $obj->param("Subject");
$author= $obj->param("Author");
$price= $obj->param("Price");
$stock= $obj->param("Stock");
$publisherName= $obj->param("pname");

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to
database:$DBI::errstr\n";

#check that the cust ID has not been used already
#since is it the primary key
my $sql = "SELECT ISBN, publisher_name from book where ISBN = '$isbn'" . "
publisher_name= '$publisherName'";

my $sth= $dbh->prepare($sql);
my $rows= $sth->execute();



if($type eq "add")
{
	if($rows > 0)
	{
		print "ISBN is already in use. Try again.\n"
	}
	else
	{
		$sql = "INSERT INTO book 
VALUES('$isbn','$title','$subject','$author','$price','$stock','$publisherName');";
		print "New Book has been added to the database.\n"
	}
} 
elsif($type eq "update")
{

		$sql = "UPDATE book SET title = '$title', subject 
= '$subject', author = '$author', price = '$price', stock = '$stock', 
publisher_name = '$publisherName' WHERE ISBN = '$isbn';";
		print "Book information has been updated.\n";
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
