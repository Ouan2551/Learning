# python collections arrays have 4 collecting data types
# 1. list => change and order allow duplicate members
# 2.Tuple = can't change value allow duplicate members
# 3.Set => unordered and unchanged no duplicate members
# 4. Dictionary => like list no duplicate members

# list => store multiple data in single variable
This_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(This_list)
# can store any data type and different data type

# find list length => use "len()"
print(len(This_list))

# find list data type => use "type()"
print(type(This_list))

# useful function "list()"
# convert string to list
string = "hello"
list_string = list(string)
print(list_string)
# convert any data type like list into list
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print(list_data)

# access list items => use index start from 1
print(This_list[1]) # forward start from 0, 1, ...
print(This_list[-1]) # backward start from -1, -2, ...
print(This_list[2:4]) # start normal:before this number
print(This_list[2:])

# Change List Items => just use index and use new data to replace it
This_list[0] = "watermelon"
This_list[1:3] = ["lime", "lemon"]
# upper code is replace value
This_list.insert(3, "pumpkin") # not replace value just insert
print(This_list)

# Add List Items
This_list.append("chill") # insert value in last member
tropical = ["mango", "pineapple", "papaya"]
This_list.extend(tropical) # insert another list in to member list
print(This_list)

# Remove List Items
This_list.remove("mango") # use "remove()" to remove member
# but if have many same value it will delete first member
This_list.pop(6) # use "pop()"  remove by using index
This_list.pop() # remove last member in list
print(This_list)

del This_list[-1] # remove member
This_list.clear() # remove list
print(This_list)
del This_list # clear list

# Loop list
This_list = ["apple", "banana", "cherry"]
for i in This_list:
    print(i)
    
# List Comprehension => just short syntax
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]
# append member have character 'a' to new_list
print(new_list)

# Sort list => use ".sort()"
This_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
Num_list = [5, 10, 1, 3, 9]
This_list.sort()
Num_list.sort()
print(This_list)
print(Num_list)

# reverse sort => inside ".sort()" use "reverse = True"
This_list.sort(reverse = True)
Num_list.sort(reverse = True)
print(This_list)
print(Num_list)
# is have a lot of function to use with "key=" but this is e.g.
This_list.sort(key = str.lower)

# Copy list => use ".copy()" or use "list()" or use ":"
copy_list = This_list.copy()
copy_list1 = list(This_list)
copy_list2 = This_list[:]
print(copy_list)
print(copy_list1)
print(copy_list2)