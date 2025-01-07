# single quote same as double quote in this case like this
print(type("Hello"))
print(type('Hello'))

# normal string
a = "hello"
print(a)

# multiple string (many line use triple quote)
b = """today i will teach you how to cooking pasta
and trick how to use pan"""
print(b)

# string is array
# array is a room store value and reach by using index
c = "Hello world"
size = len(c) # use len() to get size string
for i in range(0, size, 1):
    print(c[i])

# check string (use command "in")
txt = "The best things in life are free!"
print("free" in txt) # output true or false
# or use with if else
if "free" in txt:
    print("Yes, 'free' is present.")

# and have command "not in"
print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    

# Slicing Strings
b = "Hello, World!"
print(b[2:5]) # output code from index 2 to 5
print(b[:5]) # output code from index start to 5
print(b[5:]) # output code from index 5 to end

print(b[-2:-5]) # negative index (backward)
# structure like start:stop (num_start:num_stop)
# stop is index - 1 not real index use