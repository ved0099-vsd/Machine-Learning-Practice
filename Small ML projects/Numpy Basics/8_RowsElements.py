#Numbers[0, 1] means first row, second column.
#Numbers[1, 2] means second row, third column.

import numpy as np

Numbers = np.array([
    [10,20,30],
    [40,50,60]
])

print(Numbers[0])
print(Numbers[1])
print(Numbers[0,1])
print(Numbers[1,2])