filename = "bookdata.txt"
try:
   # If the file exists, read the data from it
   with open(filename, "r") as file:
      print("Book details in file are:")
      for line in file:
         print(line)

# file not found
except FileNotFoundError:
   print("The file did not exist and has been created.")
   print("Please enter details of at least 3 books.")
   books = []

   for i in range(1,4):
      print(f"Enter the book detail of book {i}")
      title = input("Enter title of book: ")
      author = input("Enter author of book: ")
      booktype = input("Enter book type of book: ")
      publication = input("Enter publication of book: ")
      price = input("Enter price of book: ")
      book = {"title": title, "author": author, "booktype": booktype,
              "publication": publication, "price": price}
      books.append(book)
      print()

   # Write the book data to the file
   with open(filename, "w") as f:
      for book in books:
         f.write(str(book) + "\n")
   print("Book details saved to file.")
   print("Book details in file are:")
   with open(filename, "r") as file:
      for line in file:
         print(line)