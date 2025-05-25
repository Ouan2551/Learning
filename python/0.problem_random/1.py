count = int(input())
prize = float(input())
member_chk = str(input())
total = float(count*prize)
discount = amount = 0
if (member_chk == 'y'):
    if (total <= 500.0):
        discount = total * 0.1
    elif (total > 500.0 and total < 1000.0):
        discount = total * 0.15
    else:
        discount = total * 0.2
else:
    if (total <= 500.0):
        discount = total * 0.05
    elif (total > 500.0 and total < 1000.0):
        discount = total * 0.1
    else:
        discount = total * 0.15
print("Total ", total)
print("Discount ", discount)
print("Amount", total - discount)