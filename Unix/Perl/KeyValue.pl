#!/bin/perl

%data = (1 => "altaf", 2 => "aman", 3 => "prasad", 4 => "sarah", 5 => "pratham", 6 => "mitesh");

print "Enter roll no:";
$c = <>;

# handle new line
chomp($c);

# string + num concat
print "\$data{$c} = ".$data{$c};
