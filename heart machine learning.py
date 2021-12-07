import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from matplotlib import pyplot as plt

heart_stat = pd.read_csv('C:/Users/User/PycharmProjects/UCD-Project-/data files/heart.csv')

print(heart_stat.columns)

y = heart_stat.age

heart_features = ['sex', 'chol', 'exang']

X = heart_stat[heart_features]

print(X.describe())

heart_model = DecisionTreeRegressor(max_depth=3, random_state=1234)

heart_model.fit(X, y)

print(X.head())
print("The predictions are")
print(heart_model.predict(X.head()))

text_representation = tree.export_text(heart_model)
print("The report")
print(text_representation)

fig = plt.figure(figsize=(12, 9))
_ = tree.plot_tree(heart_model, feature_names=None, filled=True)

plt.show()
