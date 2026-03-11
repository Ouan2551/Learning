arr = [16, 17, 4, 3, 5, 2]
leader_arr = []
for i in range(0, len(arr), 1):
    check = bool(True)
    for j in range(i+1, len(arr), 1):
            if (arr[i] < arr[j] and arr[i] != arr[j]):
                check = bool(False)
    if check == True:
        leader_arr.append(arr[i])
        print(arr[i], end=' ')