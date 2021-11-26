import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
fig,ax = plt.subplots()
plt.show()

heart = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/data files/heart.csv")

sns.lineplot(x=heart['chol'].head(10),y=heart['age'].head(10))