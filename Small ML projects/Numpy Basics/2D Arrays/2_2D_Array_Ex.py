import numpy as np

Marks = np.array([
    [65,78,82],
    [90,55,73],
    [45,88,95],
    [76,69,84]
])
Border = "-" * 40
print(Border)

print("1. Display the mark of the second student in the third subject.")
print(Marks[1, 2])
print(Border)

print("2. Display all three marks of the third student.")
print(Marks[2])
print(Border)

print("3. Find the total marks of each student.")
print(Border)
print("Total of first student is :")
total = print(np.sum(Marks[0]))
print(np.sum(Marks, axis=1))
print(Border)

print("4. Find the average marks in each subject.")
print(np.mean(Marks, axis=0))
print(Border)

print("5. Display all marks greater than 80.")
print(Marks[Marks > 80])
print(Border)

print("6. Count how many marks are below 70.")
print(Marks[Marks < 70])
Below = len(Marks[Marks < 70])
print(Below)

print("7. Find the highest mark in the complete array.")
print(np.max(Marks))
print(Border)

print("8. Calculate the average of all marks in the array.")
print(np.average(Marks))
print(Border)

print("9. Sort the marks of the first student in ascending order.")
print(np.sort(Marks[0]))
print(Border)

print("10. Reshape the array into 2 rows and 6 columns, then display it.")
print(Marks.reshape(2,6))