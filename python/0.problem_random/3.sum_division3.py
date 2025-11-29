x = int(input())
sum = int(0)
for i in range(1, x+1, 1):
    if i % 3 == 0:
        sum = sum + i;
print(sum)