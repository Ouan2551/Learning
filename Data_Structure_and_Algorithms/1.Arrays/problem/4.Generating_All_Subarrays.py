arr = [1, 2, 3, 4]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        for k in range(i, j+1):
            print(arr[k], end=' ')
        print()