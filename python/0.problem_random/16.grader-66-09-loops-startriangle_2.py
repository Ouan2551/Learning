x = int(input())
for i in range(0, x, 1):
    # print("i = ", i)
    if i == 0:
        print('+')
    for j in range(0, i, 1):
        # print("j = ", j)
        if i != 0 and j == 0:
            print('+', end='')
        if j == i - 1:
            print('*'); continue;
        print('*', end='')