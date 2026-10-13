#step 1 = Display

import numpy as np

print("step : Display the marks array")
Marks = np.array([45,67,88,34,76])
print(Marks)

Border = "-" * 40
print(Border)

#step 2 : Display the first element

print("step 2 : Display the first element")

print(Marks)
print(Marks[0])
print(Border)

#Step 3 : Display the last element

print("step 3 : Display the last element")

print(Marks)
print(Marks[4])
print(Border)

#step 4: Display 67, 89, 32

print("Step 4 : Display the middle elements")

print(Marks)
print(Marks[1])
print(Marks[2])
print(Marks[3])
print(Border)

# Step 5 : change 34 to 50

print("Step 5 : Change 34 to 50")

Marks[3] = 50
print(Marks)
print(Border)

#step 6 : Find total of all marks

print("Step 6 : Find total of all marks")

print(Marks)
Sum = Marks.sum()
print(Sum)
print(Border)

#step 7 : find the average of all marks

print("Step 7: Find the average of all marks")
print(Marks)
print(Marks.mean())
print(Border)

#Step 8 : Find the highest marks

print("Step 8 : Find the highest marks")
print(Marks)
print(Marks.max())
print(Border)

#step 9 : Display only marks greater than 60

print("step 9 : Display only marks greater than 60")

print(Marks)
print(Marks > 60)
print(Marks[Marks > 60])
print(Border)

#step 10: Display the number of elements in the array

print("Step 10 : Display the number of elements in the array")
print(Marks)
print(len(Marks))