#!/bin/bash

echo -n "Enter number: "
read n

i=1

while [ $i -le 10 ]
do
   echo "$n x $i = $((n * i))"
   ((i++))
done
