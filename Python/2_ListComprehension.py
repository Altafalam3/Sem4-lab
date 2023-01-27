list1=['x','y','z']

#1st part

list11 =[i*j for i in list1 for j in range(1,4)]
print(list11)


#2nd part
#list ={i*1 for i in list1]
#list2=[i*2 for i in list1]
#list3=[i*3 for i in list1]
#list4=list1+list2+list3

list12 =[i*j for j in range(1,4) for i in list1]
print(list12)
