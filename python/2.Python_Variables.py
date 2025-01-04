# python doesn't need to declare variable before use it
x = 5
y = "john"
m = n = 'a' # input value to many variable
print(type(x)) # use type() for output type of variable

# case sensitive
a = "John"
b = 'John'
# same string but use "" and '' try to output data type
# you will see result will change from char to string auto
print(type(a))
print(type(b))

# output
print(x, y, a, b) # output multiple data in one line code
print(y + a + b) # warning use same data type