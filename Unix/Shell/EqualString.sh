#!/bin/bash

echo -n "Enter first string: "
read str1
echo -n "enter second string: "
read str2

if [ $str1 = $str2 ]
then
echo " Two strings are equal"
else
echo " Two strings are not equal "
fi
