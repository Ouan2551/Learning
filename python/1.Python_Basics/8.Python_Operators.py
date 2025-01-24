# in this lesson i will write only not common used for me
print(10.5/2) # normal division
print(10.5//2) # floor division
# use "//" divide number will get result in integer data type

# logical operator (and, or, not)
x = 5
y = 20
z = 90
if x > 4 and y < 6:
    print("z_correct")
if y >= 20 or y < 10:
    print("y_correct")
print(not(z > 20 or z < 50)) # not just use like "not()" only
# not just use for reverse result from e.g. from true to false

# identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # check is same object or not
print(x is y) # check is same object or not even same value
print(x == y) # important is value same or not

# is and == different is "==" check same value or not
# but "is" use for check is object or 

# membership operators
x = ["apple", "banana"]
print("banana" in x)
print("monkey" not in x)
# check value is in list or not

# bitwise operators => use for binary numbers
# i not understand i will comeback later