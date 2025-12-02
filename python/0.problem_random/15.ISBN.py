x = str(input()); list_x = []; sum = int(0)
for i in str(x):
    list_x.append(int(i));
num_list = [10, 9, 8, 7, 6, 5, 4, 3, 2]
for i in range(0, 9, 1):
    sum += (num_list[i] * list_x[i])
# (sum + n10) % 11 == 0
for i in range(0, 10, 1):
    if (sum + i) % 11 == 0:
        list_x.append(i)
for i in list_x:
    print(i, end='')