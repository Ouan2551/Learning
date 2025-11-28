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

#___________________________________________________

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

#___________________________________________________

# Slicing Strings
b = "Hello, World!"
print(b[2:5]) # output code from index 2 to 5
print(b[:5]) # output code from index start to 5
print(b[5:]) # output code from index 5 to end

print(b[-2:-5]) # negative index (backward)
# structure like start:stop (num_start:num_stop)
# stop is index - 1 not real index use

#___________________________________________________

# Modify Strings
a = " hello bro "
b = "HELLO BRO"
print(a.upper()) # Big font
print(b.lower()) # Small font
print(a.strip()) # Remove whitespace
print(a.replace('e', 'o')) # (character_select, character_replace)
print(a.split(",")) # select char to divide string

# String concatenation (combine string)
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + ' ' + b

#___________________________________________________

# Format strings
# from before we can not combine different data type together
# but format() method can do this
age = 15
txt = f"I am {age}" # it can use for modify string and whatever
print(txt)
# using '{}' to add word in sentences
# (need 'f' front of sentences you want to transform)

txt = f"The price is {20 * 59} dollars"
print(txt)
# or using calculate in '{}'

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# output number with decimal using ':' and '.' follow variable

# Escape Characters
# Code	Result
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
# example
txt = "Hello \"I am black dog\"" # output txt with double quote
print(txt)