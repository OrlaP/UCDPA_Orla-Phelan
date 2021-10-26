import pandas as pd
netflix_data= pd.read_csv('../pythonProject/data files/netflix_titles.csv')

print(netflix_data.head())
print(netflix_data.shape)

missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:5])



#droprows= netflix_data.dropna()
#print(netflix_data.shape,droprows.shape)

dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape,dropcolumns.shape)

#cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)
cleaned_data = netflix_data.fillna(0)
