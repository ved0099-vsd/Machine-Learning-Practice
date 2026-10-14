import numpy as np

Marks = np.array([
    [60, 75, 88],
    [92, 67, 81],
    [54, 86, 73],
    [79, 95, 62]
])
print(Marks)

Border = "-" * 40
print(Border)

print("1. Display the marks of the second student.")
print(np.array(Marks[1]))

print(Border)

print("2. Display the mark 86.")
print(np.array(Marks[2,1]))

print(Border)

print("3. Display the first column of all students.")
print(Marks[:,0])

print(Border)

print("4. Find the total marks of each student.")
print(np.sum(Marks,axis=1))

print(Border)

print("5. Find the average marks in each subject.")
print(np.average(Marks, axis=0))

print(Border)

print("6. Display all marks greater than 75.")
print(Marks[Marks > 75])

print(Border)

print("7. Count how many marks are greater than or equal to 80.")
Marks[Marks >= 80]
print(len(Marks>=80))

print(Border)

print("8. Find the minimum mark in the entire array.")
print(np.min(Marks))

print(Border)

print("[x] 9. Display the shape and size of the array.")
print(np.shape(Marks))
print(np.size(Marks))

print(Border)

print("10. Sort the fourth student's marks in descending order.")
print(np.sort(Marks[3][::-1]))