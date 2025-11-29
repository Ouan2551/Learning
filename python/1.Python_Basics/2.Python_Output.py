x = int(20)
print(x)

# print without new line
print("Hello", end=' ')
print("World")

# print the same thing on the same line (control manual)
x = 50
for i in range(1,x + 1,1):
    if i % 10 == 0:
        print(i)
    else:
        print(i, end=' ')