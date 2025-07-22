import pandas as pd

my_dataset = {'cars': ["BMW", "Volvo", "Ford"], 'passings': [3, 7, 2] }

my_var = pd.DataFrame(my_dataset)

print(my_var)
print("pandas version : ",pd.__version__)