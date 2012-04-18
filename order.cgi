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
my($paytype,$cardnum,$isbn,$quan,$custid);
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;
$paytype= $obj->param("payType");
$cardnum= $obj->param("cardNum");
$isbn= $obj->param("ISBN");
$custid= $obj->param("custID");
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
	#get today's date
	#get the localtime for the date
        my($sec,$min,$hour,$mday,$mon,$year,$wday,$wday,$yday,$isdst) = localtime;
        my $curYear= $year + 1900;
        my $yearString= "";
        $yearString .= $curYear .= "-";
        $mon = $mon + 1;
        if($mon < 9)
        {
       		$yearString .= "0";
        }
       	$yearString .= $mon .= "-";
        if($mday < 10)
        {
         	$yearString .= "0";
        }
       	$yearString .= $mday;

	$sql = "INSERT INTO orders VALUES(default,'$paytype','$cardnum', 
	'$yearString','Placed','$custid')";

	my $sth = $dbh->prepare($sql);
	$sth->execute();

	$sql = "SELECT MAX(OID) from orders";
	$sth = $dbh->prepare($sql);
	$sth->execute();
	my @result = $sth->fetchrow_array();

	$sql = "INSERT INTO contain VALUES($result[0],'$isbn','$quan')";
	$sth = $dbh->prepare($sql);
	$sth->execute();

	print "Your order has been successfully placed.\n";
}

$sth->finish();

