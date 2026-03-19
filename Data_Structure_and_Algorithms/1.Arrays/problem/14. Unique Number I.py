arr = [2, 3, 5, 4, 5, 3, 4]
for i in range(0, len(arr), 1):
    count = 0
    for j in range(0, len(arr), 1):
        if(arr[i] == arr[j]):
                count += 1
    if count != 2:
        [
            print(arr[i])
        ]