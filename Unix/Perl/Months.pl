@weekdays = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');

print "Enter a number from 1 to 7: ";
$number = <>;

if ($number >= 1 && $number <= 7) {
   print "$weekdays[$number - 1]\n";
}
else {
   print "Invalid number\n";
}