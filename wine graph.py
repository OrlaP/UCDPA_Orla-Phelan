import pandas as pd
import matplotlib.pyplot as plt
fig,ax = plt.subplots()

data= pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/data files/winemag-data-130k-v2.csv")

x = data['country'].head(25)
y = data['points'].head(25)

ax.plot(x,y)


ax.plot(x,y, marker="v", linestyle="--", color="r")

plt.show()