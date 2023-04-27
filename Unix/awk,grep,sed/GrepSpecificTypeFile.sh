#!/bin/bash

echo "Enter the file extension: "
read extension

egrep -w ".*\.$extension$" <<< "$(ls)"

