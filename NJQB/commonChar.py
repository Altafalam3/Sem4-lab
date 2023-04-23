str1 = 'Java'
str2 = 'PHP'

# Find common characters
common_chars = sorted(set(str1) & set(str2))

# Check if there are any common characters
if len(common_chars) == 0:
   print("No common characters")
else:
   print("Common characters:", ", ".join(common_chars))
