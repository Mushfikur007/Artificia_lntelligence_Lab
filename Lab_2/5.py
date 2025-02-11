import numpy as np

matrix = np.random.randint(1, 100, (5, 5))  
row_sums = matrix.sum(axis=1)  
print(matrix)
print("Row-wise sums:", row_sums)