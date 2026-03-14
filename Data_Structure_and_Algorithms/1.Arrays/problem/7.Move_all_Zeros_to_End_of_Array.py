arr = [1, 2, 0, 4, 3, 0, 5, 0]
arr_new = []; count = 0
for i in range(0, len(arr), 1):
    if(arr[i] != 0):
        arr_new.append(arr[i])
    else:
        count += 1
for j in range(0, count, 1):
    arr_new.append(0)
for i in range(0, len(arr), 1):
    print(arr_new[i], end=' ')