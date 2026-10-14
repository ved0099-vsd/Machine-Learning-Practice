import numpy as np

Marks = np.array([
    [72, 85, 91],
    [64, 78, 55],
    [93, 67, 82],
    [59, 88, 74]
])
print(Marks)

Border = "-" * 40
print(Border)

print("1. Display the mark 78.")
print(Marks[1,1])

print(Border)

print("2. Display the last two columns of all students.")
print(Marks[:, 1:3])

print(Border)

print("3. Calculate the total marks of each student.")
print(np.sum(Marks, axis=1))

print(Border)

print("4. Calculate the average marks in each subject.")
print(np.average(Marks, axis=0))

print(Border)

print("5. Display all marks greater than 80.")
print(Marks[Marks > 80])

print(Border)

print("6. Count the marks below 70.")
print(Marks[Marks < 70])
print(len(Marks[Marks < 70]))

print(Border)

print("7. Find the minimum and maximum marks.")
print(np.max(Marks))
print(np.min(Marks))

print(Border)

print("8. Sort the second student's marks in descending order.")
print(np.sort(Marks[1])[::-1])

print(Border)

print("9. Display the shape, size, and dimensions.")
print(np.shape(Marks))
print(np.size(Marks))
print(np.ndim(Marks))

print(Border)

print("10. Reshape the array into 2 rows and 6 columns.")
print(Marks.reshape(2,6))