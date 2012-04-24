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
my($type,$name,$city);
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;
$type= $obj->param("type");

$name= $obj->param("Name");
$city= $obj->param("city");

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to
database:$DBI::errstr\n";

#check that the cust ID has not been used already
#since is it the primary key
my $sql = "SELECT publisher_name from publisher where publisher_name = 
'$name'";
my $sth= $dbh->prepare($sql);
my $rows= $sth->execute();

if($type eq "add")
{
	if($rows > 0)
	{
		print "Publisher is already in use. Try again.\n"
	}
	else
	{
		$sql = "INSERT INTO publisher 
VALUES('$name','$city');";
		print "New Publisher has been added to the database.\n"
	}
} 
elsif($type eq "update")
{

		$sql = "UPDATE publisher SET city = '$city' WHERE 
publisher_name = '$name';";
		print "Publisher information has been updated.\n";
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
