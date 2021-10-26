a=3
b=3
c=4

sub= a+b+c
div= a/b/c
multi=a*b*c

print (sub)
print (div)
print (multi)

height = 550
weight = 60

bmi = (height/weight**2)
print(bmi)

type(bmi)
print(type(bmi))

fam = [0,1,2,3,4,5]
fam[5]
print(fam)
max(fam)
print(max(fam))
print(fam[3])
fam = fam.index(2)
print(fam)
kit = 2
hall = 5

house = ["kitchen", kit, "hallway", hall]
print(house)


a = "hello_Python"
print(a)
print(type(a))

import pandas as pd

df=pd.read_csv("../pythonProject/data files/foster.csv")
print (df)

print(df.describe())
df.loc[1:3]
print(df.loc[1:3])








