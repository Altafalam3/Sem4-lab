a = 5
b = "7"

# Try to add the values a and b
try:
   result = a + b
   print(result)
except TypeError:
   try:
      b1 = int(b)
      c = a + b1
      print(c)
   except ValueError:
      try:
         result = a + float(b)
      except Exception as e:
         print(e)