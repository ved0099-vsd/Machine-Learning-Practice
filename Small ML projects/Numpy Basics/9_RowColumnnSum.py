#axis=1 calculates the sum of each row.
#axis=0 calculates the sum of each column.

import numpy as np

Numbers = np.array([
    [10,20,30],
    [40,50,60]
])

print("Total :",np.sum(Numbers))
print("Rows Sums :", np.sum(Numbers, axis=1))
print("Columns sums :", np.sum(Numbers,axis=0))