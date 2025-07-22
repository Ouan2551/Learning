import pandas as pd

# series => like column
a = [1, 7, 2]
a1 = {"a": 1, "b": 7, "c":2} # key/value like dictionary
my_var = pd.Series(a)
my_var1 = pd.Series(data=a, index=["x", "y", "z"]); # custom label
my_var2 = pd.Series(a1)

print("series")
print(my_var)
print("index 0 : ", my_var[0])
print("         ")

print("custom index")
print(my_var1)
print("index x : ", my_var1["x"]) # output custom label

print(my_var2)

# data_frames => like whole table
data = {"calories":[100, 200, 300], "time":[10, 20, 30]};
my_var = pd.Series(data=data)
print(my_var)