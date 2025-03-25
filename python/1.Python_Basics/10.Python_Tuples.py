# Tuples => store multiple item in single variable (work with index)
# tuples can't change value like list
# tuples use '()' not like list use '[]'
this_tuple = ("hello", "world")
print(type(this_tuple))
print(this_tuple)

# length tuple
print(len(this_tuple))

# creat tuple with 1 item
this_tuple = ("apple",) # have comma then python recognize this is tuple
print(type(this_tuple))

#NOT a tuple (not have comma)
this_tuple = ("apple")
print(type(this_tuple))

# tuple can store different data type
tuple1 = ("hello", 50, True, 'a')

# tuple constructor
this_tuple = tuple(("banana", "apple", "grape", "papaya")) # don't forget 2 round brackets
print(this_tuple)

# Access tuple 0 for first value
print(this_tuple[1]) # use index
# negative index
print(this_tuple[-1]) # use -1 for last value
# range of index
print(this_tuple[0:2]) # in last number 2 it like this <2 but not like this <= 2
print(this_tuple[:2])
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[-4:-1])
if "apple" in this_tuple:
    print("have apple text in this tuple")