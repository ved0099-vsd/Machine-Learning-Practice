import numpy as np

Marks = np.array([
    [72, 84, 91],
    [65, 77, 69],
    [88, 93 ,81],
    [54, 62, 70]
])

print("1. Display the marks of the third student")
print(np.array(Marks[2]))
Border = "-" * 40

print("2.Display the mark 77")
print(np.array(Marks[1,1]))
print(Border)

print("3.display the last two columns of all students")
print(np.array(Marks[:,1:3]))
print(Border)

print("4.Calculate the total marks of each student")
print(np.sum(Marks, axis=1))
print(Border)

print("5.calculate the average marks in each subject")
print(np.average(Marks, axis=0))
print(Border)

print("6.Display marks greater than 80")
print(Marks[Marks > 80])
print(Border)

print("7.Display how many marks are below 70")
below = (Marks[Marks < 70])
print(below)
print(len(Marks[Marks < 70]))
print(Border)

print("8.find the highest mark in the array")
print(np.max(Marks))
print(Border)

print("9.Find the arrays shape, size and number of dimensions")
print(np.shape(Marks))
print(np.size(Marks))
print((np.ndim(Marks)))
print(Border)

print("10.Sort the first students marks in ascending order")
print(np.sort(Marks[0]))