import pandas as pd

df = pd.read_csv('winemag-data-130k-v2.csv')

print(df.shape)

missing_values_count = df.isnull().sum()
print(missing_values_count)

print(df.loc[:,"price"])
#price column missing 8996 values and needs to be cleaned

# replacing missing values in price column
# with median of that column
df['price'] = df['price'].fillna(df['price'].median())
print(df['price'])

