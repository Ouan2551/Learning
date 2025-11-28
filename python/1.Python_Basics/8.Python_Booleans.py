# booleans is a data type in python have value 'true' and 'false'
print(10 > 9)
print(10 == 9)
print(10 < 9)

# custom section just use for make easily revise lesson
print("__________________")

# use bool() to get value of bool in any data type
print(bool("Hello"))
print(bool(15))

# Almost any value is evaluated to True but have some except
# Any string is True, except empty strings
# Any number is True, except 0
# Any list, tuple, set, and dictionary are True except empty
# None bool value is "false"

print("__________________")

# but if you create class and return 0 you will get value false
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

print("__________________")

# function can return value booleans
def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

print("__________________")

# python have build in function use for check data type
x = "Hello World"
print(isinstance(x, int))
print(isinstance(x, str))