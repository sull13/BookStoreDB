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

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to
database:$DBI::errstr\n";


my $sql = "INSERT INTO orders VALUES(default,'$paytype','$cardnum', 
'2012-04-16','Placed','$custid')";

my $sth = $dbh->prepare($sql);
$sth->execute();

$sth->finish();

print $custid;
