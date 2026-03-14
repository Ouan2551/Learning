arr = [1, 2, 3, 4, 5, 6]
arr_new = []; arr_trail = []
d = int(input())
arr_trail = arr.copy()
# for i in range(0, len(arr_trail), 1):
#     print(arr_trail[i], end=" ");

for i in range(0, d, 1):
    arr_new.clear(); arr_new.append(arr_trail[len(arr)-1])
    for j in range(0, len(arr)-1, 1):
        arr_new.append(arr_trail[j]);
    arr_trail = arr_new.copy();
    # print(arr_trail)

for i in range(0, len(arr), 1):
    print(arr_new[i], end=' ')