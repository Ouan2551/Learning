import numpy as np
# create array using array()
arr = np.array(['a', 'b', 'c']) # like convert list to array
# you can convert whatever to array e.g. list, dictionary, tuples
print(type(arr))
print(arr)

# Dimension of array
# 1) O-D arrays
arr = np.array(42)
print(arr)
# 2) 1-D arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)
# 3) 2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)