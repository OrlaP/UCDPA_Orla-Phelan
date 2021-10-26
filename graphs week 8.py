import pandas as pd
import matplotlib.pyplot as plt
fig,ax = plt.subplots()

data= pd.read_csv("../pythonProject/data files/GBvideos.csv")

x = data['channel_title'].head(5)
y1 = data['views'].head(5)
y2 = data['likes'].head(5)

ax.plot(x,y1)
ax.plot(x,y2)

ax.plot(x,y1, marker="v", linestyle="--", color="r")

plt.show()