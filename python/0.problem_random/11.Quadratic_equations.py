a = list(map(int, input().split()))
part_square_root = float(((a[1]**2) - (4*a[0]*a[2]))**0.5)
result1 = (-a[1] + part_square_root)/(2*a[0])
result2 = (-a[1] - part_square_root)/(2*a[0])
format_result1 = "{:.2f}".format(result1)
format_result2 = "{:.2f}".format(result2)
print("x = ", format_result1); print("x = ",format_result2);