prices = [100, 180, 260, 310, 40, 535, 695]
profits = int(0)
for i in range(1, len(prices), 1):
    if prices[i] > prices[i-1]:
        profits += prices[i] - prices[i-1]
print(profits)