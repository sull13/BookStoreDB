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
my($isbn,$quan);
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;
$isbn= $obj->param("ISBN");
$quan= $obj->param("quan");

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to
database:$DBI::errstr\n";

#check that the isbn is valid
my $sql = "SELECT isbn from book where isbn = '$isbn'";
my $sth= $dbh->prepare($sql);
my $rows= $sth->execute();

if($rows < 1)
{
	print "ISBN not found.\n"
}

else
{
	#check to make sure there is enough of a given book left in the 
	#database

	my $sql = "SELECT title,stock from book where ISBN = '$isbn'";
	my $sth= $dbh->prepare($sql);
	my $rows= $sth->execute();
	my @stock = $sth->fetchrow();

	#update the amount of stock left in the book
	my $reorderedStock = $stock[1] + $quan;
	$sql = "Update book SET stock = '$reorderedStock' where ISBN = '$isbn';";
	$sth = $dbh->prepare($sql);
	$sth->execute();

	print "You have successfully reordered $quan copies of $stock[0]\n";

}

$sth->finish();

