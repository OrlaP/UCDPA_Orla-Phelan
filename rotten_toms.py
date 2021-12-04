import pandas as pd

df = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/data files/rotten_tomatoes_movies.csv")

y = df.tomatometer_rating
df_features=['content_rating' ,'genres', 'tomatometer_status', 'tomatometer_count', 'audience_rating' ,'audience_count', 'tomatometer_rotten_critics_count']
X = df[df_features]

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))