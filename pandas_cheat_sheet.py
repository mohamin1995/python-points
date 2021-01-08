import pandas as pd

df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

print(df)

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(df)

print(pd.Series([1, 2, 3, 4, 5]))
print(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
print(wine_reviews.shape)
print(wine_reviews.head())

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print(reviews.country)
print(reviews['country'])
print(reviews['country'][0])

# index based selection
print(reviews.iloc[0]) # first row of data frame
print(reviews.iloc[:, 0]) # all rowsm first column
print(reviews.iloc[[0, 1, 2], 0])

#label based selection
print(reviews.loc[0, 'country'])
print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

reviews.set_index("title")

# conditional selection
reviews.loc[reviews.country == 'Italy']
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
reviews.loc[reviews.country.isin(['Italy', 'France'])]
reviews.loc[reviews.price.notnull()]


reviews['critic'] = 'everyone' # change all column values to 'everyone'

print(reviews.points.describe())
print(reviews.points.mean())
print(reviews.taster_name.unique())
print(reviews.taster_name.value_counts())

# map
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

#grouping and sorting

reviews.groupby('points').points.count()
reviews.groupby('points').price.min()
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
reviews.groupby(['country']).price.agg([len, min, max])
reviews.sort_values(by='len', ascending=False)
reviews.sort_values(by=['country', 'len'])


# data types and missing values

print(reviews.price.dtype)
print(reviews.dtypes) # Alternatively, the dtypes property returns the dtype of every column in the DataFrame
reviews[pd.isnull(reviews.country)]
reviews.region_2.fillna("Unknown")
df.isna().sum()