import numpy as np

a = np.array([[2,4,6,8,6],[23,56,45,10,83],[98,12,34,78,78],[21,63,78,84,53]])

print(a)
b = a[::2, 1::2]

print(b)

"""
print(a)
result = a[np.arange(a.shape[0]) % 2 == 0, 1::2]
print(result)


'''
Return the array of even rows and odd columns from following array 
'''
print(a)
b = a[::2, 1::2]

print(b)
"""
