import numpy as np

Numbers = np.array([10,20,30,40,50])
print(Numbers)

Border = ("-" * 40)
print(Border)

print(Numbers[0])
print(Numbers[2])
print(Numbers[4])

print(Border)

print(Numbers + 5)
print(Numbers * 3)
print(Numbers - 10)

print(Border)

print("Array Properties")

print("Dimensions :",Numbers.ndim)
print("Shape: ",Numbers.shape)
print("Size :", Numbers.size)
print("Datatype :",Numbers.dtype)


