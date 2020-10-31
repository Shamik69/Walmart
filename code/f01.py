import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path= 'C:/Users/User/PycharmProjects/Walmart/data'

df= pd.read_csv(f'{path}/features.csv')
print(df)
for col in df.columns:
    print(f'{col}: {df[col].unique()}\n'
          f'{df[col].shape}')
print(df.shape)