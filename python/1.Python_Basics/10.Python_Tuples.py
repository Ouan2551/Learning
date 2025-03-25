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
this_tuple = tuple(("banana", "apple", "grape")) # don't forget 2 round brackets
print(this_tuple)