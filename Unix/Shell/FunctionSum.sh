#!/bin/bash

sum()
{
s=0
x=1

while [ $x -le $1 ]
do
((s=$s+$x))
((x=$x+1))
done

return $s
}

sum $1
echo "The sum of sequence is : $?"