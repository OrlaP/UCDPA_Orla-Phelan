import numpy as np
from numpy import random
import pandas as pd

df = pd.read_csv('C:/Users/User/PycharmProjects/UCD-Project-/data files/heart.csv')

heart = np.array(df[1:], dtype=float)

print(heart)

x = random.randint(1000)

print(x)

x1 = random.randint(1000, size=(4, 6))

print(x1)

print(np.__version__)
