arr = [100, 180, 260, 310, 40, 535, 695]
profits = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        profits += arr[i] - arr[i-1]
print(profits)