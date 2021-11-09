import re
import pandas as pd

df = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject/data files/winemag-data-130k-v2.csv")

taster_twitter_handle = df['taster_twitter_handle']
print(taster_twitter_handle)
regex = r"@\W*"

result = re.findall(regex, str(taster_twitter_handle[0:25]))
print(result)

