x = int(input())
for i in range(2, x+1, 1):
    # print("hello")
    check_num = int(i); prime_num = bool(True)
    for j in range(2, check_num, 1):
        if check_num % j == 0 and check_num != 0 and check_num != j:
            prime_num = False
    if prime_num == True:
        print(check_num, end=' ')