import pandas as pd

df = pd.read_csv('House prices ireland.csv')

print(df.shape)
print(df.head())
#missing data
missing_values_count = df.isnull().sum()
print(missing_values_count[0:8])

#cleaning up missing data from value (84 missing)
clean_list= df.dropna()
print(df.shape,clean_list.shape)


