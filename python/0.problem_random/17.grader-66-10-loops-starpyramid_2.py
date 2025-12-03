x = int(input())
for i in range(-(x-1), x+3, 1):
    for j in range(0, x+1, 1):
        if i == j:
            print('*', end='')
        # print("(i, j) = ", (i, j), end='')
        # if j == i-2:
        #     print(" ")