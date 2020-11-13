import pandas as pd
import matplotlib.pyplot as plt

path = 'C:/Users/User/PycharmProjects/Walmart/data'

df= pd.read_csv(f'{path}/features.csv')
df0= df.dropna()
for col in df.columns:
    print(f'{col}: {df[col].unique()}\n'
          f'{col}: {df0[col].unique()}\n')
print(df0, '\n', df)