import numpy as np

A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

for i in range(len(A[1])):
    A[i] = A[i][::-1]
print(A)
A = (np.array(A) + 1) % 2

print(A.tolist())

print([2] * 3)

