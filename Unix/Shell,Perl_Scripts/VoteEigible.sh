#!/bin/bash

echo Enter age
read a
if [ $a -ge 18 ];
then
	echo You are eligible to vote
else
	echo You are not eligible to vote
fi
