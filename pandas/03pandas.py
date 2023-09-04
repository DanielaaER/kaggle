import pandas as pd


wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")


# print(wine_reviews)

# print("\n", wine_reviews.shape)

# print("\n", wine_reviews.shape[1])
# print("\n", wine_reviews.shape[0])

print("\n", wine_reviews.head())



wine_reviews2 = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print("\n", wine_reviews2.head() )