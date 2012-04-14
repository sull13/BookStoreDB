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
my($isbn,$title,$author,$isbnSearch,$titleSearch,$authorSearch);
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

if($author eq '')
{	
	$authorSearch = "REGEXP '^.*'";
        #print $authorSearch;
}
else
{
	$authorSearch= "= '$author'";
	#print $authorSearch;
}
if($title eq '')
{
	$titleSearch= "REGEXP '^.*'";
}
else
{
	$titleSearch= "= '$title'";
}
if($isbn eq '')
{
	$isbnSearch= "REGEXP '^.*';";
}
else
{
	$isbnSearch= "= '$isbn';";
}

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to 
database:$DBI::errstr\n";
 
my $sql = "SELECT ISBN,title,subject,author,price,publisher_name"
	 . " from book WHERE author ".  $authorSearch
         . " AND title " . $titleSearch
         . " and ISBN " . $isbnSearch;
my $sth = $dbh->prepare($sql);
$sth->execute();

my @rows;
my @fields;

while(@rows = $sth->fetchrow()) {
	#my @result = @rows;
	#push(@fields,@result);
	#print @rows; 
	#print "<br>";
	print $rows[0];
	print "<br>";
	print $rows[1];
        print "<br>";
	print $rows[2];
        print "<br>";
	print $rows[3];
        print "<br>";
	print $rows[4];
        print "<br>";
	print $rows[5];
        print "<br>";
	print "<br>";
	
}

$sth->finish();



