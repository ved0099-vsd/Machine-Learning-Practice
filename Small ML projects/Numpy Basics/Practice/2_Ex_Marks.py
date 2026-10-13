import numpy as np

Marks = np.array([45,67,89,32,76,91,54,83])
print(Marks)

Border = "-" * 40
print(Border)

#Step 1: Display the first four elements

print("Step 1 : Display the first four elements")
print(Marks)
print(Marks[0:4]) #slicing
print(Border)

#step 2 : Display the last three elements

print("step 2 :Display the last three elements")
print(Marks)
print(Marks[-3:])
print(Border)

#step 3: Display every second element, starting from the first.

print("step 3 :Display every second element, starting from the first.")
print(Marks)
print(Marks[::2])
print(Border)

# step 4: Display the array in reverse order

print("Step 4 : Display the array in reverse order")
print(Marks)
print(Marks[::-1])
print(Border)

#Step 5: Change 89 to 95 and display the updated array.

print("Step 5: Change 89 to 95 and display the updated array")
print(Marks)
Marks [2] = 95
print("Updated marks are :",Marks)
print(Border)

#Step 6 :Add 5 to every element and display the result without changing the original array.

print("Step 6 :Add 5 to every element and display the result without changing the original array")
print(Marks)
print(Marks + 5)
print("Updated marks are :",Marks)
print(Border)

#Step 7 : Display all marks that are greater than or equal to 75

print("#Step 7 : Display all marks that are greater than or equal to 75")

print(Marks[Marks >= 75])
print(Border)

#Step 8: Count how many marks are below 60.

print("#Step 8 : Count how many marks are below 60")

print(Marks)
below_60 = Marks[Marks <= 60]
print(below_60)
print(len(below_60))
print(Border)

#Step 9 : find the sum and average of the marks

print(Marks)
Sum = np.sum(Marks)
print(Sum)
print(Border)

print("Average")
Average = np.mean(Marks)
print(Average)
print(Border)

#Step 10 : Sort the marks in ascending order

print("Step 10 : Sort the marks in ascending order")
print(np.sort(Marks))