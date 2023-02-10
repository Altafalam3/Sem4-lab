dict1 = {1:"www.google.com" , 2:"www.tsec.edu" ,
         3:"www.asp.net" , 4:"www.abcd.in" }

l1 = list(dict1.values())
t1 = []

#print(l1)

for i in l1:
    j = i.split('.')
    t1.append(j[2])

t1 = tuple(t1)
print(t1)
