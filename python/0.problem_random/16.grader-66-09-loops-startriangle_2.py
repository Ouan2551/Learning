x = int(input())
for i in range(0, x+1, 1):
    if i == 0:
        print('+')
    else:
        for j in range(0, i+1):
            if j < 2:
                print('+', end='')
            elif j != i-1:
                print('*', end='')
            else:
                print('*')