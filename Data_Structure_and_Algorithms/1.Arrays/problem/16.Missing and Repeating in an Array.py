arr = [4, 3, 6, 6, 2, 1, 1]; arr.sort(); arr_max = arr[len(arr) - 1]
# find num twice
for i in range(0, len(arr), 1):
    count = int(0)
    for j in range(i+1, len(arr), 1):
        if arr[i] == arr[j]:
            print(arr[i]); i = j; break

# find missing num
for i in range(1, arr_max+1, 1):
    check = bool(False);
    for j in range(0, len(arr), 1):
        if (i == arr[j]):
            check = True;
    if check == False:
        print(i)