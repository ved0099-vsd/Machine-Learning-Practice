import pandas as pd

Numbers = pd.Series([10,20,30,40,50])
print(Numbers)

print("-" * 40)

print(Numbers[1])
print(Numbers[3])

print("-" * 40)

print(Numbers.sum())
print(Numbers > 25)
print(Numbers[Numbers > 25])