import os.path

# Define the file name
filename = "bookdata.txt"

# Check if the file exists
if os.path.isfile(filename):
    # If the file exists, read the data from it
    with open(filename, "r") as f:
        data = f.read()

    # If the file is empty, prompt the user to enter book details
    if not data:
        print("The file is empty.")
        print("Please enter details of at least 3 books.")
        books = []
        for i in range(3):
            title = input("Enter title of book: ")
            author = input("Enter author of book: ")
            booktype = input("Enter book type of book: ")
            publication = input("Enter publication of book: ")
            price = input("Enter price of book: ")
            book = {"title": title, "author": author, "type": booktype,
                    "publication": publication, "price": price}
            books.append(book)

        # Write the book data to the file
        with open(filename, "w") as f:
            for book in books:
                f.write(str(book) + "\n")

        print("Book details saved to file.")

    else:
        # If the file is not empty, print the book data
        print("The following book details were found in the file:")
        print(data)

else:
    # If the file does not exist, create an empty file and prompt the user to enter book details
    with open(filename, "w") as f:
        pass
    print("The file did not exist and has been created.")
    print("Please enter details of at least 3 books.")
    books = []
    for i in range(3):
        title = input("Enter title of book: ")
        author = input("Enter author of book: ")
        booktype = input("Enter book type of book: ")
        publication = input("Enter publication of book: ")
        price = input("Enter price of book: ")
        book = {"title": title, "author": author, "type": booktype,
                "publication": publication, "price": price}
        books.append(book)

    # Write the book data to the file
    with open(filename, "w") as f:
        for book in books:
            f.write(str(book) + "\n")
    print("Book details saved to file.")
