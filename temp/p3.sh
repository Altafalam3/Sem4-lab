echo Enter a number 
read a
sum=0

for((i=1;i<=a;i++))
do
	sum=$(( i+sum ))
done
echo Sum of n numbers is : $sum
