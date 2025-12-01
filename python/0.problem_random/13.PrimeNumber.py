count = int(0); x = int(input())
for i in range(2, x+1, 1):
    check_prime = bool(True)
    for j in range(2, i, 1):
        if i % j == 0:
            check_prime = False
    if check_prime == True:
        print(i, end = ' '); count += 1
print(' '); print(count);