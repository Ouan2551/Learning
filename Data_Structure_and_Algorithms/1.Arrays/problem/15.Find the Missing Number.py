arr = [8, 2, 4, 5, 3, 7, 1]
arr.sort(); arr_max = arr[len(arr) - 1];
for i in range(1, arr_max+1, 1):
    check = bool(False);
    for j in range(0, len(arr), 1):
        if i == arr[j]:
            check = True
    if check == False:
        print(i)