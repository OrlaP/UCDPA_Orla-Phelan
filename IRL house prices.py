import pandas as pd
import numpy as np

df = pd.read_csv('House prices ireland.csv')

print(df.shape)
print(df.head())
#missing data
missing_values_count = df.isnull().sum()
print(missing_values_count[0:8])

#cleaning up missing data from value (84 missing)
clean_list= df.dropna()
print(df.shape,clean_list.shape)

clean_list['C02343V02817'] = df['C02343V02817'].replace(['-'],['0'])

print (clean_list['C02343V02817'])
