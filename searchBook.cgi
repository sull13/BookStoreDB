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
my($isbn,$title,$author,$sub,$pub,
   $isbnSearch,$titleSearch,$authorSearch,$subSearch,$pubSearch,$type);
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;
$isbn= $obj->param("ISBN");
$title= $obj->param("Title");
$author= $obj->param("Author");
$sub = $obj->param("sub");
$pub= $obj->param("pub");
$type= $obj->param("type");

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to 
database:$DBI::errstr\n";
 

#the variable for the sql query
my $sql= "SELECT ISBN,title,subject,author,price,publisher_name from book ";

#this variable is used to determine the first "and" needed
my $conditionCount= 0;

#check if at least one value was entered into any of the fields
#and add the WHERE clause if that's the case
if( ($author ne "") || ($title ne "") || ($isbn ne "") || ($sub ne "") || ($pub ne "") ) 
{
	$sql= $sql . "WHERE ";
	#add the author to the search if it's not empty
	if($author ne "")
	{
		$author= "%" . $author . "%";
        	$author= $dbh->quote($author);
	        $sql= $sql . "author LIKE " . $author  . " ";
        	$conditionCount++;
	}
	if($title ne "")
	{
		$title= "%" . $title . "%";
        	$title= $dbh->quote($title);
        	if($conditionCount > 0)
        	{
                	$sql= $sql . "AND ";
        	}
        	$sql= $sql . "title LIKE " . $title . " ";
        	$conditionCount++;
	}
	if($isbn ne "")
	{
		$isbn= "%" . $isbn . "%";
        	$isbn= $dbh->quote($isbn);
        	if($conditionCount > 0)
        	{
                	$sql= $sql . "AND ";
        	}
        	$sql= $sql . "ISBN LIKE " . $isbn . " ";
        	$conditionCount++;
	}
	if($sub ne "")
	{
		$sub= "%" . $sub . "%";
        	$sub= $dbh->quote($sub);
        	if($conditionCount > 0)
        	{
                	$sql= $sql . "AND ";
        	}
        	$sql= $sql . "subject= " . $sub . " ";
        	$conditionCount++;
	}
	if($pub ne "")
	{
		$pub= "%" . $pub . "%";
        	$pub= $dbh->quote($pub);
        	if($conditionCount > 0)
        	{
                	$sql= $sql . "AND ";
        	}
        	$sql= $sql . "publisher_name LIKE " . $pub . " ";
        	$conditionCount++;
	}

	$sql = $sql . ";";	
}

my $sth = $dbh->prepare($sql);
$sth->execute();

my @rows;
my @fields;

while(@rows = $sth->fetchrow()) {
	print "ISBN: $rows[0]";
	print "<br>";
	print "Title: $rows[1]";
        print "<br>";
	print "Subject: $rows[2]";
        print "<br>";
	print "Author(s): $rows[3]";
        print "<br>";
	print "Price: $rows[4]";
        print "<br>";
	print "Publisher: $rows[5]";
        print "<br>";
	if($type eq "update")
	{
		print "<a href='AddUpdateBook.php?type=$type&ISBN=$rows[0]'>Modify</a>";
	}
	else
	{
		 print "<a href='order.php?isbn=$rows[0]&title=$rows[1]'>Order</a>";
	}
	print "<br>";
	print "<br>";
}

$sth->finish();



