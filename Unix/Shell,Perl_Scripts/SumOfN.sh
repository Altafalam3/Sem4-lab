echo Enter a number 
read a
n=$(($a))
sum=1
while [ $n -ge 1 ]
do
	sum=$((sum*n))
	n=$((n-1))
done
echo Sum of $a numbers is : $sum
