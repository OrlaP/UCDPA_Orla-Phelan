import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

heart = pd.read_csv("C:/Users/User/PycharmProjects/UCD-Project-/data files/heart.csv")
sns.catplot(x= 'age', y='chol', hue='sex',  data=heart)
plt.show()