import numpy as np

# create an 8x3 array of numbers from 10 to 34
arr = np.arange(10, 34).reshape(8, 3)

# split the array into 4 equal parts
part1, part2, part3, part4 = np.split(arr, 4)

print("Part 1:")
print(part1)
print("\nPart 2:")
print(part2)
print("\nPart 3:")
print(part3)
print("\nPart 4:")
print(part4)

'''
Create a 8*3 array for numbers from 10 to 34 . Split the array into 4 equal parts
'''
