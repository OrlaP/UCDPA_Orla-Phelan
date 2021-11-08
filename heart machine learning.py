import pandas as pd

heart_stat = pd.read_csv('C:/Users/User/PycharmProjects/pythonProject/data files/heart.csv')

print(heart_stat.columns)

y = heart_stat.target

heart_features = ['age','sex','chol', 'exang']

X = heart_stat[heart_features]

print (X.describe())

from sklearn.tree import DecisionTreeRegressor

heart_model = DecisionTreeRegressor(random_state=1)

heart_model.fit(X,y)

print(X.head())
print("The predictions are")
print(heart_model.predict(X.head()))
