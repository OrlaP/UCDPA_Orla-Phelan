import pandas as pd

house_price = pd.read_csv('House prices ireland.csv')

print(house_price.columns)

y = house_price.VALUE

house_features = ['TLIST(Q1)']


X = house_price[house_features]

print (X.describe())

from sklearn.tree import DecisionTreeRegressor

house_model = DecisionTreeRegressor(random_state=1)

house_model.fit(X,y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(house_model.predict(X.head()))
