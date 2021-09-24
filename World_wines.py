import pandas as pd

df = pd.read_csv('winemag-data-130k-v2.csv')

print(df.shape)

missing_values_count = df.isnull().sum()
print(missing_values_count)

