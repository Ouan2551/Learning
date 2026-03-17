arr = [1, 2, 3, 1, 4, 5]; k = 3
for i in range(0, len(arr), 1):
    for j in range(i+1, len(arr), 1):
        if ((arr[i] == arr[j]) and (abs(i-j) <= k)):
            print("Yes"); exit()
print("No")