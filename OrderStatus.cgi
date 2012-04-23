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
my($OID);
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;
$OID = $obj->param("OID");

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to 
database:$DBI::errstr\n";
 
my $sql = "SELECT status from orders where OID= '$OID';";
my $sth = $dbh->prepare($sql);
$sth->execute();

my @rows;
my @fields;

while(@rows = $sth->fetchrow()) {

	print "Order ID: $OID";
	print "<br>";
	print "Current Status: $rows[0]";
        print "<br>";
}

$sth->finish();



