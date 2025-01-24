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