import numpy as np

#Step 1: Display the array

print("Step 1 : Display the marks array")
Marks = np.array([
    [78,85,90],
    [67,72,80],
    [92,88,95],
    [55,60,65]
])

print(Marks)

Border = "-" * 40
print(Border)

#Step 2 : Display the marks of first student

print("Step 2 : Display the marks of first student")
print(Marks)
print(Border)
print("Marks of first student are")
print(Marks[0])
print(Border)

#Step 3:Display the marks of the third student

print("3. Display the marks of the third student.")
print(Marks)
print(Border)
print("Marks of third student are")
print(Marks[2])

#Step 4: Display the mark 72.

print("Step 4: Display the mark 72.")
print(Marks)
print(Border)
print(Marks[1, 1])

#step 5: Display the marks of the first two students

print("Step 5 : Display the marks of the first two students")
print(Marks[0:2])
print(Border)

#Step 6: Display all marks in the second subject(second column)

print("Step 6 :  Display all marks in the second subject(second column")

print(Marks[:,1])
print(Border)

#Step 7: Find the total marks of each student (row-wise).

print("Step 7: Find the total marks of each student (row-wise)")
print(np.sum(Marks, axis=1))
print(Border)

#step 8:find the average marks in each subject (column - wise)

print("step 8:find the average marks in each subject (column - wise)")
print(np.mean(Marks, axis=0))
print(Border)

#9. Display all marks greater than 80

print("9. Display all marks greater than 80")
print(Marks > 80)
print(Marks[Marks > 80])
print(Border)

#10. Find the number of rows and columns in Marks.

print("10. Find the number of rows and columns in Marks.")

print(np.info(Marks))
# OR
print(Marks.shape)
