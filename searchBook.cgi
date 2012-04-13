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
my($isbn,$title,$author);
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

#connect to the MySQL database
        $dbh = DBI->connect
        ("DBI:mysql:database=$db:host=$host:mysql_socket=$socket",
                                $user,
                                $password)
                                or die "Can't connect to 
database:$DBI::errstr\n";
 
my $sql = "SELECT title from book WHERE author = '$author'";
my $tagID = $dbh->prepare($sql);
$tagID->execute();
my @rows;
while(@rows = $tagID->fetchrow_array()) {
	#my @result = @rows;
	print @rows; 
	print "<br>";

}
$tagID->finish();



#my $tagID = $dbh->prepare($sql);
#$tagID->execute();

#my @test;
#$tagID->bind_columns(\@test);
#$tagID->fetch();
#$tagID->finish();

#print "Test 1= @test[1]";
#print "test search";


