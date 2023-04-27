#!/bin/bash

echo "Enter a year:"
read year

# divideable by 4  and (not by 100 or divideable by 400)

if [ $((year % 4)) -eq 0 ] && [ $((year % 100)) -ne 0 ] || [ $((year % 400)) -eq 0 ]
then
  echo "$year is a leap year"
else
  echo "$year is not a leap year"
fi