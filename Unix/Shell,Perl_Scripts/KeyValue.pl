#!/usr/bin/perl

%data = (1 => "altaf", 2 => "aman", 3 => "prasad", 4 => "sarah", 5 => "pratham", 6 => "mitesh");

print "Enter roll no:";
$c = <>;

chomp($c);

print "\$data{$c} = $data{$c}\n";