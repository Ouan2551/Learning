# python have 3 type of numbers
# 1) integer (int)
# 2) decimal (float) and scientific numbers ("e")
# 3) complex use j for imaginary part
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert type
x = float(x)
y = int(y)
print(x, y)
# but you can't convert type complex to another

# random numbers
# first import library
import random
print(random.randrange(1, 10))