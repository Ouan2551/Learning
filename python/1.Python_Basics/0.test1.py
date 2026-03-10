import math
days = int(input()); sum = int(0)
for i in range(1, days+1, 1):
    sum += math.pow(2, i-1);
    # print("sum : ", sum);
print("money : ", sum)