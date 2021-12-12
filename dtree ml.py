# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier   # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn import tree
from matplotlib import pyplot as plt

#load dataset
heart = pd.read_csv('C:/Users/User/PycharmProjects/UCD-Project-/data files/heart.csv')

print(heart.head())

feature_cols = ['sex', 'chol', 'fbs', 'exang', 'age']
X = heart[feature_cols]  # Features
y = heart.target  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy,
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
#plot the graph for decision tree
fig = plt.figure(figsize=(12, 9))
_ = tree.plot_tree(clf, feature_names=feature_cols, filled=True)

plt.show()