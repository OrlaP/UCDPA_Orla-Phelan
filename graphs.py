import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

heart = pd.read_csv("C:/Users/User/PycharmProjects/UCD-Project-/data files/heart.csv")
sns.catplot(x='age', y='chol', hue='sex',  data=heart)
plt.show()
