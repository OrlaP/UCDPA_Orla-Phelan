import pandas as pd

canadian_youtube = pd.read_csv("../pythonProject/data files/CAvideos.csv")
british_youtube = pd.read_csv("../pythonProject/data files/GBvideos.csv")

concat_data= pd.concat([canadian_youtube, british_youtube])

print(concat_data)

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')

merged_data= pd.merge(left,right,on='video_id')

print(left.shape, right.shape)
print(join_data.shape, merged_data.shape)
merged_data= pd.merge(left,
right [['video_id','views','likes','dislikes']],
on='video_id’
how='left/right/outer')
