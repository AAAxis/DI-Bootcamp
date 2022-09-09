import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import onehotenconder

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# print(df.head())
# setosa = df.loc[df['species'] == 'setosa'].head()
# print(setosa)

# virginica = df.loc[df['species'] == 'virginica'].head()
# print(virginica)

dummies = pd.get_dummies(y)
print(dummies)

# y = categorical and nominal