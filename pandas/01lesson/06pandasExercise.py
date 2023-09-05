import pandas as pd


ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews)



