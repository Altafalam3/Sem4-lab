#!/bin/bash

echo -n "Enter Principal amount:"
read p
echo -n "Enter time period:"
read t
echo -n "Enter rate of interest:"
read r

si=$(((p * r * t) / 100))
echo "Simple interest is $si"

total=$(($p + $si))
echo "Total amt is $total"
