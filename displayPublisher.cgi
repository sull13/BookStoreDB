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
my $dbh;
my $db="sulliv49";
my $user="sulliv49";
my $password="redcreed2";
my $host="localhost";
my $socket="/tmp/mysql-51.sock";

my $obj = new CGI;

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to
database:$DBI::errstr\n";

#list all the customers currently in the database
my $sql = "SELECT * from publisher;";
my $sth = $dbh->prepare($sql);
$sth->execute();

my @rows;

while(@rows = $sth->fetchrow()) {

        print "Publisher: $rows[0]";
        print "<br>";
        print "City: $rows[1]";
        print "<br>";
        print "<a href='AddUpdatePublisher.php?type=update&PUB=$rows[0]'>Modify</a>";
        print "<br>";
        print "<br>";
}
$sth->finish();
