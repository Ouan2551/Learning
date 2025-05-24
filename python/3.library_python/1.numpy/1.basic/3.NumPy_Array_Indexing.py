# access array element by using index
import numpy as np
arr = np.array([1, 2, 3])
# it can't use () with not another brackets for declare it from tuple or list because
# array() only get 1 object e.g. np.array(1, 2) not work it need another data like tuple list dict before
print(arr[0])

# access 2d array element
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1, 2])

# access 3d array element
arr = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(arr[1, 1, 0])