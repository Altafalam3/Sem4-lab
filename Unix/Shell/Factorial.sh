#!/bin/bash

echo Enter a number
read a
sum=0

for((i=1;i<=a;i++))
do
	sum=$(( i+sum ))
done

echo Sum from 1 to $a is : $sum

echo Enter a number
read a

n=$(($a))
pro=1

while [ $n -ge 1 ]
do
	pro=$((pro*n))
	n=$((n-1))
done

echo Factorial of $a  is : $pro
