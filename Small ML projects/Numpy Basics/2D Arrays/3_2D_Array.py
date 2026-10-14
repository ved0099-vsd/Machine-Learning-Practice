import numpy as np

Marks = np.array([
    [70, 85, 90],
    [55, 68, 75],
    [92, 88, 79],
    [60, 72, 95]
])

print(Marks)
Border = "-" * 40
print(Border)

print("1. Display the marks of the fourth student.")
print(np.array(Marks[3]))

print(Border)

print("2. Display the mark 88")
print(Marks[2, 1])

print(Border)

print("3. Display the first two columns of all students.")
print(Marks[:, 0:2])  #Slicing

print(Border)

print("4. Calculate the total marks of each student.")
print(np.sum(Marks[0]))
print(np.sum(Marks[1]))
print(np.sum(Marks[2]))
print(np.sum(Marks[3]))

print(Border)

print("5. Calculate the average marks in each subject.")
print(np.average(Marks, axis=0))

print(Border)

print("6. Display all marks greater than 80.")
print(Marks[Marks > 80])

print(Border)

print("7. Count the number of marks below 70.")
print(Marks[Marks < 70])

print(Border)

print("8. Find the minimum and maximum marks.")
print(np.max(Marks))
print(np.min(Marks))
print(Border)

print("9. Display the shape and total number of elements.")
print(np.shape(Marks))
print(np.info(Marks))

print(Border)

print("10. Reshape the array into 3 rows and 4 columns.")
print(Marks.reshape(3,4))