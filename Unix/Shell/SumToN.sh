#!/bin/bash

echo Enter a number
read a
sum=0

for((i=1;i<=a;i++))
do
	sum=$(( i+sum ))
done

echo Sum from 1 to $a is : $sum
