#  All programs are uploaded given by Sachi Mam

### Assignment 3
```
Return the array of even rows and odd columns from following array 
a=[[2,4,6,8,6],[23,56,45,10,83],[2,5,33,22,88]]



Create a 8*3 array for numbers from 10 to 34 and split the array into 4 parts.
```


### Assignment 4
```
Write a function that can add any number of iterables when passed as a parameter to it . include appropriate docstring for function .Show the execution with various cases in python 



Given a sequence of n values x1, x2, ..., xn and 4 window size k>0, the k-th moving average of the given sequence is defined as follows:

The moving average sequence has n-k+1 elements as shown below. The
moving averages with k=4 of a ten-value sequence (n=10) is shown below

i 1 2 3 4 5 6 7 8 9 10

Input 10 20 30 40 50 60 70 80 90 100
y1 25 = (10+20+30+40)/4

y2 35 = (20+30+40+50)/4

y3 45 = (30+40+50+60)/4

y4 55 = (40+50+60+70)/4

y5 65 = (50+60+70+80)/4

y6 75 = (60+70+80+90)/4

y7 85 = (70+80+90+100)/4

Thus, the moving average sequence has n-k+1=10-4+1=7 values.
Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3 .



Accept an 1-D array from user. Write a function to convert it into a matrix
called Vandermonde matrix. It is obtained as follows:
Each ith column of the matrix is obtained by raising the element of array
to power i and maximum value of power dictates the number of columns
in the matrix. Also it is one of the parameters to the function generating this marix. Another parameter to the function will be Boolean variable 'ascending'.

If ascending is true, power of the element will be in increasing order
starting from 0. If ascending is not specified, power of the ith column of
the matrix will be (p-i-1) where p is the number of columns.

e.g. M=[1,2,3]
1)
matrix=
1 1 1 
1 2 4
3 5 9 
(when p=3 and ascending = True)

2)
matrix= 
1 1 1 
4 2 1
9 3 1
(when p=3 and ascending = False) .

```

### Assignment 8
```
Create two lists numbers and multipliers , scan through multipliers list , take each of the" value "and multiply the number from the numbers list at the position equals to index of value by a.

If multipliers list exhaust before numbers handle the exception with following message "program haulted since multiplier list exhausted" .

If either of the list name is referred incorrectly handle the exception by printing the message the" list does not exist".

At the end print the message multiplication of two list is done.


Write a program to add two values a and b , and integer value is assigned to a however while defining b by mistakenly it was enclosed with a quotes by the programmer handle the exception so that b can be added with the integer value a (here b  would have been int/float if not in quotes ) Display appropriate messages and use nested exception handling .
```


### Assignment 9
```
Write a program to read a file called  bookdata.txt if file does not exist create an empty file and display appropriate message to user.

If empty file is created ask user to enter details of minimum 3 books, for every book user should enter title,author,booktype, publication and price.

Store information of each book in the form of dictionary, list of all such books should be written to file then open the file read book details and display it.
```


### Assignment 10
```
Using Tkinter create a calculator having following appearance and
functionalities.
Functionalities to include:
1. Calculator should support basic operations like addition,
subtraction, multiplication and division.
2. User should be able to type number (containing any number of
digits) in the text area.
3. When user clicks on any operator button, contents from text
area should get cleared so that user can enter second number
(containing any number of digits).
4. When user clicks on ‘=’ button result of operation should be
displayed in text area. Any contents from text area should be
cleared before displaying the result.
5. Clicking on clear button should clear the contents from text area.
6. Add suitable icon and title for the application window.
```

### Assignment 13
```
Create a dataframe having following columns:
• ISBN (unique number for each book)
• Title
• Author
• Publication
• Year Published
• Price
• Copies sold of first edition
• Copies sold in second edition
• Copies sold in third edition
You can use any of the studied approach to create dataframe. Add
minimum 10 records to the dataframe. Perform following
operations on dataframe using appropriate functions:
1. Display the number of rows and columns in dataframe
2. Give the descriptive statistics of the created dataset.
3. Display distinct publication names for the dataset.
4. Display the book title and author names published by “Metro
Publication”
5. Rename columns “Copies sold in first edition”, “Copies sold in
second edition” and “Copies sold in third edition”to FE, SE and
TE respectively
6. Add a column “Average sale” to your dataframe derived as
(average of FE, SE and TE) * Price.
7. Display the details of books grouped by author.
8. For each group obtained in above query display maximum
value of Average sale.
9. Reshape your dataframe such that rows will show ‘Author’,
column will show “Publication” and values will be ‘Title’ of
book.
```

### Assignment 14
```
Using scipy library, perform following linear algebraic operations:
1. Solve the system of linear equations:
a. 9x + 6y – 5z + 2w = 17
b. 4x + 5y – 7z + 3w = 10
c. -3x - 4y + 2z - 5w = 20
d. 6x + y + 9z - w = 23

2. Perform the following operations on a matrix
𝐴 = [
5 3 2
6 9 −3
1 7 4
]
a. Find Inverse of matrix A.
b. Find Kronecker product of A with B= [
3 −1
2 −5
]
c. Find determinant of matrix A
```

### Assignment 15
```
1: Create a web application using Flask to display the Books
available in the library when the ‘books’ endpoint is visited. For
each book, display ISBN number, Book title, Author and publication.
Also facilitate the search of book by ISBN number. For this the ISBN
number should be passed as parameter and the details of only that
book will be displayed. (Use GET, render template, redirect,
jsonify methods).

2:Create a web app using Flask to display the result of a user. If
marks are less than 50, redirect user to the ‘failed’ web page and
display the appropriate result. Otherwise, redirect user to ‘passed’
web page and display the appropriate result on that page. (Use
redirect, jsonify and other methods as needed).
```
