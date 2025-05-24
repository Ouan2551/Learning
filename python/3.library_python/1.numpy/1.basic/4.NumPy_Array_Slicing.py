# slicing in python mean take element from one index to another index
# structure arr[start_index : end_index - 1]
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:3]) # from structure end_index - 1 = 3 then end_index = 2 (output from 1 index to 2 index)

# now it have step
# structure arr[start_index : end_index - 1 : step]
print(arr[0 : 5 : 2]) # it like loop with += 2 (step = 2)

# after this just use structure to get what code do
print(arr[:2]) # 2 mean end_index
print(arr[2:])