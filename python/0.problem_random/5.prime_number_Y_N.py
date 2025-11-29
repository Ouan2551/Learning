x = int(input())
for i in range(2, x, 1):
    # print(i)
    if x % i == 0 and x != 0:
        print("is not prime"); quit();
print("is prime")