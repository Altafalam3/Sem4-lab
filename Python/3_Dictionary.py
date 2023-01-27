t = (4,5,6,2,3,4,5,1,2,6,4)

dict1 = {}

for i in t:
    j = t.count(i)
    dict1[i] = j

print(dict1)


'''
set1 = set()
for i in t:
    set1.add(i)

print(set1)

for i in set1:
    j = t.count(i)
    dict1[i] = j

print(dict1)
'''
