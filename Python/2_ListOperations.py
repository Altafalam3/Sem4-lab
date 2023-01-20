list1=[]

numbers=int(input("Enter the total numbers:"))

for i in range(numbers):
    num=int(input("Enter the number:"))
    list1.append(num)

ev=0
od=0

for i in list1:
    if i%2==0:
        ev+=i
    else:
        od+=i

#inserting even num sum and odd num sum
t1=(ev,od)
print(t1)
