import pandas as pd

rt_critic = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/data files/rotten_tomatoes_critic_reviews.csv")
rt_reviews = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/data files/rotten_tomatoes_movies.csv")

print(rt_critic.head())
print(rt_reviews.head())

left = rt_critic.set_index(['rotten_tomatoes_link'])
right = rt_reviews.set_ndex(['rotten_tomatoes_link'])

merged_data = pd.merge(left, right, on='rotten_tomatoes_link')

print(merged_data.head(10))

