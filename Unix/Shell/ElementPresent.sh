#!/bin/bash

echo -n "enter elements of array"
read -a array

echo -n "enter the element to be searched"
read num

for val in "${array[@]}"
do
   if [ $num == $val ]
   then
      echo "element is present in the array"
      exit
   else
      continue
   fi
done