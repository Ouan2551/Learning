x = int(input())
for i in range(2, x+2, 2):
    if i % 20 == 0:
        print(i)
    else:
        print(i, end=' ')