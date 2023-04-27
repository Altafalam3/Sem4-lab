#!/bin/bash 

echo "Enter the file path:"
read filename

echo -n "No of lines are: "
echo `wc -l $filename`
echo -n "No of words are: "
echo `wc -w $filename`
echo -n "No of characters: "
echo `wc -c $filename`