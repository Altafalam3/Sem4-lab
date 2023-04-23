# Get number of students
num_students = int(input("Enter the number of students: "))

# Initialize lists for storing student names and total marks
names = []
marks = []

# Get student names and marks
for i in range(num_students):
    name = input("Enter the name of student {}: ".format(i+1))
    names.append(name)
    marks_list = []
    for j in range(3):
        mark = int(input("Enter the mark for subject {}: ".format(j+1)))
        marks_list.append(mark)
    marks.append(marks_list)

# Calculate total marks for each student using lambda and store them in a list
total_marks = list(map(lambda x: sum(x), marks))

# Get the second lowest total marks
second_lowest_marks = sorted(set(total_marks))[1]

# Find the students with the second lowest marks and print their names
for i in range(num_students):
    if sum(marks[i]) == second_lowest_marks:
        print(names[i])
