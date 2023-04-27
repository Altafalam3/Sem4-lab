#!/bin/perl

print " Enter number to check prime: ";
$num=<STDIN>;

chop($num);

$flag=0;
for($i=2; $i<$num; $i++)
{
   if ($num % $i==0)
   {
      $flag=1;
      break;
   }
}

if ($flag==1)
{
print " $num is not prime\n ";
}
else
{
print "$num is prime\n";
}