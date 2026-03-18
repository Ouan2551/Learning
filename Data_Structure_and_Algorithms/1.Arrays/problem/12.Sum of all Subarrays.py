arr = [1, 4, 5, 3, 2]; sum = int(0)
for i in range(0, len(arr), 1):
    for j in range(i+1, len(arr), 1):
        for k in range(i, j+1, 1):
            sum += arr[k]
for i in range(0, len(arr), 1):
    sum += arr[i]
print(sum)