#!/bin/bash

echo -n "Enter filename: "
read fname

if test -d $fname
then
   echo "$fname is a directory"
else
   if test -f $fname
   then
      echo "$fname is a file"
   else
      echo "$fname is not valid"
      exit 1
   fi
fi
