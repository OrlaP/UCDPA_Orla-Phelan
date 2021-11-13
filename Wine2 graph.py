import pandas as pd
import matplotlib.pyplot as plt
fig,ax = plt.subplots()

df = pd.read_csv('C:/Users/User/PycharmProjects/pythonProject/data files/winemag-data-130k-v2.csv')

x = df['country'].head(10)
y1 = df['price'].head(10)

ax.plot(x,y1)

ax.plot(x,y1, marker="v", linestyle="--", color="r")

plt.show()