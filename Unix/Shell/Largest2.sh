echo "Enter first number"
read a

echo "Enter second number"
read b

echo "Enter third number"
read c

if [ $a -gt $b ] && [ $a -gt $c ]
then
   echo "$a is greatest number"
else
   if [ $b -gt $c ]
   then
      echo "$b is greatest number"
   else
      echo "$c is greatest number"
   fi
fi