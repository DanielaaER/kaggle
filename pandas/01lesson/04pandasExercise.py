import pandas as pd

fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
print(fruits)

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'], index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews)



