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

# not tuple (not have comma)
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
    

# Change value tuples (convert tuple to list and then change value after that change back to tuple)
this_list = list(this_tuple)
this_list[0] = "monkey" # change value using index
this_tuple = tuple(this_list)

# Add value
this_list = list(this_tuple)
this_list.append("Hello") # this method convert to list before
this_tuple = tuple(this_list)
add_tuple = ("watermelon", ) # add tuple to tuple
this_tuple += add_tuple
print(this_tuple)

# Delete value
this_list = list(this_tuple)
this_list.remove("Hello") # this method convert to list before
this_tuple = tuple(this_list)
print(this_tuple)
# or delete all of tuple by this method
del this_tuple
# print(this_tuple) # get error because you delete tuple 

# unpack tuples
fruits = ("apple", "banana", "cherry")
# extract value to variable
f1, f2, f3 = fruits
print(f1)
print(f2)
print(f3)
# using "Asterisk*" => if number of variable is less than value in tuple add '*'
# to front of variable and then this variable will be list
fruits = ("apple", "banana", "cherry", "mango", "watermelon", "lemon")
f1, *f2, f3 = fruits
print(f1)
print("list f2 : ", f2)
print("type list f2 : ", type(f2))
print(f3) # f3 will always be last value

# loop tuples
fruits = ("apple", "banana", "cherry", "mango", "watermelon", "lemon")
print("__________for_loop__________")
# for loop
for i in fruits:
    print("fruit : ",i)
for i in range(len(fruits)): # look like in c++ like this for(int i; i <= fruits.size(); i++)
    print(fruits[i])
print("__________while_loop__________")
# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
    
# join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuples
fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2 # double value in tuples
print(my_tuple)

# return how much value in tuples using count
# (put everything you want to count it over there)
print("count apple text : ", my_tuple.count("apple"))

# search in tuple for value and return index (where value live)
print("location apple text : ", my_tuple.count("apple"))