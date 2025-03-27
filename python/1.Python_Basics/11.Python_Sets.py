# set unordered unchangeable can't duplicate unindex but can remove and add item
# set can store multiple data type in one set
this_set = {'A', 'B', 'C'}
print(type(this_set))
print(this_set)

# important output value
this_set1 = {"apple", "banana", "cherry", True, 1, 2}
this_set2 = {"apple", "banana", "cherry", False, 0, 2}
print(this_set1)
print(this_set2)
# value "True" and '1' set will think is same value
# value "False" and '0' set will think is same value

# length sets
print("length this_set :",len(this_set))

# convert to set using list()
this_set = list(('a', 'b', 'c')) # double brackets warning!
print(type(this_set))