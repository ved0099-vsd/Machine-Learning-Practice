import numpy as np

Marks = np.array([
    [68, 85, 92],
    [74, 59, 81],
    [91, 77, 64],
    [55, 88, 79]
])

print(Marks)

Border = "-" * 40
print(Border)

print("1.Display the mark 81.")
print(Marks[1, 2])

print(Border)

print("2.Display the first two columns of all students.")
print(Marks[:,:2])
print(Border)

print("3.Calculate the total marks of each student.")
print(np.sum(Marks, axis=1))
print(Border)

print("4.Calculate the average mark in each subject.")
print(np.average(Marks, axis=0))
print(Border)

print("5.Display all marks greater than 80.")
print(Marks[Marks > 80])
print(Border)

print("6.Count how many marks are below 70.")
print(Marks[Marks < 70])
print(len(Marks[Marks < 70]))

print("7.Sort the third student's marks from highest to lowest.")
print(np.sort(Marks[2][::-1]))
print(Border)

print("8.Display the lowest and highest marks in the array.")
print(np.max(Marks))
print(np.min(Marks))
print(Border)

print("9.Display the shape, size, and number of dimensions.")
print(np.shape(Marks))
print(np.size(Marks))
print(np.ndim(Marks))

print("10.Reshape the array into 3 rows and 4 columns.")
print(Marks.reshape(3,4))
print(Border)