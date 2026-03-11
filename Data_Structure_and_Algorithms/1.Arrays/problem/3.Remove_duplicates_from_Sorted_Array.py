arr = [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8]
arr_complete = []
for i in range(0, len(arr), 1):
    # print("checking i = ", arr[i])
    check = bool(False)
    for j in range(i+1, len(arr), 1):
        # print("checking j = ", arr[j]);
        if (arr[i] == arr[j]):
            check = bool(True); break
    if check == False:
        arr_complete.append(arr[i])

for i in range(0, len(arr_complete), 1):
    print(arr_complete[i], end=' ')