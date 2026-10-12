import numpy as np

Numbers = np.array([10,20,30,40,50])
print(Numbers)

Border = ("-" * 40)
print(Border)

print("Indexing")

print(Numbers[0])
print(Numbers[2])

print(Border)

print("Array change")

Numbers[2] = 69
Numbers[4] = 90

print(Numbers)

print(Border)

print("Calculations")

print(Numbers + 10)
print(Numbers * 5)
print(Numbers / 6)

print(Border)

print("Array Properties")

print("Dimension :", Numbers.ndim)
print("Shape",Numbers.shape)
print("Size :", Numbers.size)
print("Datatype :",Numbers.dtype)

print(Border)

print("Values Condition")

print(Numbers)
print(Numbers > 55)
print(Numbers[Numbers > 55])

