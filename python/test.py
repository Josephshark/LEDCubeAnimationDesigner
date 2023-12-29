from ledcube import create_cube
import numpy as np

"""
Test the create_cube function.
n = 3
print(create_cube(n))

"""

# Using the builtin np functions
np_matrix = np.ones((3,3,3), np.int8)
print(np_matrix)

print("After setting the middle to zero")

np_matrix[1,1,1] = 0
print(np_matrix)

mat_array = np.asarray(np_matrix)

print(mat_array)