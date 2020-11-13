import pandas as pd
import numpy as np
from sklearn import preprocessing, cluster
import matplotlib.pyplot as plt

path = 'C:/Users/User/PycharmProjects/Walmart/data'

x0 = pd.read_csv(f'{path}/output.csv')

x = pd.DataFrame(preprocessing.scale(x0[['sales', 'Size']]),
                 columns=['sales', 'Size'])
# c0 = cluster.KMeans(3).fit_predict(x[['holiday', 'Size']])
# x['holiday cluster'] = c0
c1 = cluster.KMeans(3).fit_predict(x[['sales', 'Size']])
x['workday cluster'] = c1
plt.scatter(x0['Store'], x0[x0['Type']==0]['holiday'], c=x0['Type'], cmap='rainbow')
plt.legend()
plt.show()
plt.scatter(x0['Store'], x0['holiday'], c=x0['Type'], cmap='rainbow')
plt.show()
