# Define the two lists
numbers = [1, 2, 3, 4, 5]
multipliers = [2, 4, 1, 3]

# Try to iterate through the multipliers list and multiply the corresponding number
# in the numbers list by the current multiplier value
try:
    for i in range(max(len(numbers),len(multipliers))):
        numbers[i] *= multipliers[i]
except IndexError:
    print("Program halted since list exhausted.")
except NameError:
    print("A list does not exist.")
else:
    print("Multiplication of two lists is done")
finally:
    print(numbers)
    print(multipliers)