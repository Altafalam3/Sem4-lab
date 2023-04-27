#!/bin/bash

echo Enter a number
read a
sum=0

for((i=1;i<=a;i++))
do
	sum=$(( i+sum ))
done

echo Sum from 1 to $a is : $sum


echo "enter length"
read n1
echo "enter width"
read n2

area=`expr $n1 \* $n2`
echo -n "Area of rectangle is :"
echo $area

p1=`expr $n1 + $n2`
peri=`expr 2 \* $p1`
echo -n "Perimeter of rectangle is :"
echo $peri