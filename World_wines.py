import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../pythonProject/data files/winemag-data-130k-v2.csv')

print(df.shape)
print(df.head())
print(df.tail())

missing_values_count = df.isnull().sum()
print(missing_values_count)

print(df.loc[:,"price"])
#price column missing 8996 values and needs to be cleaned

# replacing missing values in price column
# with median of that column
df['price'] = df['price'].fillna(df['price'].median())
print(df['price'])
# selecting designation column
print(df.loc[:,'designation'])
# removed column 'designation'
print(df.drop(['designation'], axis=1))
# create wine dictionary
wine = {'country', 'description', 'points', 'price', 'province', 'title', 'variety', 'title'}

df2 = pd.DataFrame(wine)

print(df2)

#api request
import requests
request = requests.get('https://api.globalwinescore.com/')
print(request.status_code)

#create graphs







