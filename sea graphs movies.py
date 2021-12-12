import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rotten_toms=pd.read_csv('C:/Users/User/PycharmProjects/UCD-Project-/data files/rotten_tomatoes_movies.csv')
sns.distplot(rotten_toms[np.array("genres", string)], kde=False)
plt.show()