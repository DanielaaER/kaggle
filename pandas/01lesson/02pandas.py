import pandas as pd

dataframe1 = pd.Series([1, 2, 3, 4, 5])

print("\n",dataframe1)

dataframe2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

print(dataframe2)
