import pandas as pd

movies_ = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/tmdb_5000_movies.csv")
credits = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/tmdb_5000_credits.csv")

print(movies_.head())
print(credits.head())

movies_.rename(columns={'id_':'movie_id'})

left = movies_.set_index(['movie_id'])
right = credits.set_index(['movie_id'])

merged_data= pd.merge(left,right,on='movie_id')

print(merged_data.head(10))
