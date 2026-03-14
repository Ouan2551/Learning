import sys
arr = [4, 4, 4, 4]; k = int(3)
operation_saved = int(0); max_num = -sys.maxsize; check = bool(True)
for i in range(0, len(arr), 1):
    max_num = max(arr[i], max_num);

for i in range(0, len(arr), 1):
    test_num = int(arr[i]); count = int(0);
    while test_num <= max_num or test_num > max_num:
        if(test_num == max_num):
            operation_saved += count; break
        elif (test_num > max_num):
            # print("test1")
            check = False; break;
        else:
            # print("test")
            test_num += k; count += 1
            # print(test_num - 3); print(test_num);
        # print("test")

if (check == True):
    print(operation_saved)
else:
    print(-1)