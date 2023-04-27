#!/bin/bash

# read -a arr

# define an array
arr=(5 2 8 1 6)

# initialize first element as largest
largest=${arr[0]}

# iterate over array and compare
for i in ${arr[@]}
do
   if [ $i -gt $largest ]
   then
      largest=$i
   fi
done

echo "The largest element in the array is: $largest"
