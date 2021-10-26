import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
fig,ax = plt.subplots()

data= pd.read_csv("../pythonProject/data files/GBvideos.csv")

sns.lineplot(x=data['video_id'].head(5),
y=data['views'].head(5))

plt.show()