fname = input("enter fname:")

lname = input("enter lname:")

print(fname,lname)

for i in range(len(lname)-1,-1,-1):
    print(lname[i],end="")

print(" ",end="")

for i in range(len(fname)-1,-1,-1):
    print(fname[i],end="")
