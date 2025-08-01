import numpy as np
import time

# NumPy routines which allocate memory and fill arrays with value
a = np.zeros(4);                print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.zeros((4,));             print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.random_sample(4); print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
print("___________________________________")

# NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument
a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
print("___________________________________")

# NumPy routines which allocate memory and fill with user specified values
a = np.array([5,4,3,2]);  print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}")
a = np.array([5.,4,3,2]); print(f"np.array([5.,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
print("___________________________________")

# Operations on vectors
# 1) Indexing
a = np.arange(10); print(a); print(a[2].shape); print(a[2]); print(a[-1])

# index must be within the range of the vector or they will produce and error
try:
    c = a[10]
except Exception as e:
    print("The error message you'll see is:")
    print(e)
    
# 2) Slicing
a = np.arange(10)
print(f"a = {a}")

#access 5 consecutive elements (start:stop:step)
c = a[2:7:1];     print("a[2:7:1] = ", c)

# access all elements index 3 and above
c = a[3:];        print("a[3:]    = ", c)

# access all elements below index 3
c = a[:3];        print("a[:3]    = ", c)

# access all elements
c = a[:];         print("a[:]     = ", c)

# 3) Single vector operations
b = -a; print(b)
b = np.sum(a); print(b)
b = np.mean(a); print(b)
b = a**2; print(b)

print("___________________________________")

# Vector Dot product

a = np.array([1, 2, 3, 4])
b = np.array([-1, -2, -3, -4])
def my_dot(a, b):
    x = 0
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x
print(my_dot(a, b)) # using normal loops
print(np.dot(a, b)) # vectorization

print("___________________________________")

# Matrix
a = np.zeros((1, 5)) # 1 rows 5 columns                    
print(f"a shape = {a.shape}, a = {a}")                     

a = np.zeros((2, 1)) # 2 rows 1 columns                                                
print(f"a shape = {a.shape}, a = {a}") 

a = np.random.random_sample((2, 5)) # 2 rows 5 columns
print(f"a shape = {a.shape}, a = {a}") 

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 3 rows 3 columns
print(f"a shape = {a.shape}, a = {a}")

# Indexing
a = np.arange(6); print(a)
# using -1 mean let numpy calculate rows by yourself
a = np.arange(6).reshape(-1, 2); print(a)
a = np.arange(12).reshape(6, -1); print(a)
print(a[2,1])

# Slicing
# warning stop is like index -1 before
a = np.arange(start=1, stop=200, step=2).reshape(-1, 1); print(a)