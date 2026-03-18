arr = [1, 3, 2];
for i in range(1, len(arr), 1):
    if (i % 2 == 0 and arr[i] >= arr[i-1]):
        temp = int(arr[i]); arr[i] = arr[i-1]; arr[i-1] = temp
    elif ((i % 2 != 0) and (arr[i] <= arr[i-1])):
        temp = int(arr[i]); arr[i] = arr[i-1]; arr[i-1] = temp
print('[', end ='')
for i in range(0, len(arr), 1):
    if (i < len(arr) - 1):
        print(arr[i], end = ' ')
    else:
        print(arr[i], end = ']')