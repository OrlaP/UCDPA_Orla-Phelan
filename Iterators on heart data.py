import pandas as pd
df = pd.read_csv("/data files/heart.csv")

df2= pd.DataFrame(df)

print(df2)

#1
Row_list = []
for index, rows in df2.iterrows():
    my_list=[rows.chol]
    Row_list.append(my_list)
    print(Row_list)

#2 data from fosters dataset
January = [235, 131, 518, 155, 207, 325, 237, 181, 227, 317, 91, 285, 89, 397, 272, 77, 287, 20]

for numbers in January:
    if numbers >= 100:
        print('High!')


#3

# Initialize an empty dictionary
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv("/data files/heart.csv", chunksize = 10):
    # Iterate over the "chol" column in DataFrame
    for entry in chunk["chol"]:
        if entry in counts_dict.keys():
            counts_dict[entry] += 150
        else:
            counts_dict[entry] = 150

# Print the populated dictionary
print(counts_dict)