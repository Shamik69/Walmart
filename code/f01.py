import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/User/PycharmProjects/Walmart/data'

df0 = pd.read_csv(f'{path}/train.csv')
df1 = pd.read_csv(f'{path}/stores.csv')


def fn01(df=df0):
    for col in df.columns:
        print(f'{col}: {df[col].unique()}\n'
              f'{df[col].unique().shape}')
    print(df.shape)


store_holiday_sales = []
store_non_holiday_sales = []
sales = []
for i in df0['Store'].unique():
    dept_sales_h = []
    dept_sales_n = []
    x = df0[df0['Store'] == i]
    for j in x['Dept'].unique():
        y = x[x['Dept'] == j]
        non_holiday_sales = y[y['IsHoliday'] == False]['Weekly_Sales']
        holiday_sales = y[y['IsHoliday'] == True]['Weekly_Sales']
        dept_sales_h.append(round(sum(holiday_sales), 2))
        dept_sales_n.append(round(sum(non_holiday_sales), 2))
        store_holiday_sales.append([i, j, round(sum(holiday_sales), 2), 1])
        store_non_holiday_sales.append([i, j, round(sum(non_holiday_sales), 2), 0])
    sales.append([i, round(sum(dept_sales_h), 2), round(sum(dept_sales_n), 2)])
# output_df0= pd.DataFrame(sales, columns=['Store', 'Dept', 'sales', 'holiday'])
# output_df1= pd.DataFrame(store_non_holiday_sales, columns=['Store', 'Dept', 'sales', 'holiday'])
# output_df0= output_df0.append(output_df1)
x1 = pd.DataFrame(sales, columns=['Store', 'holiday', 'workday']).join(df1[['Type','Size']])
x1['sales']= round(x1['holiday']+x1['workday'], 2)
x1['Type']= x1['Type'].map({'A':0, 'B':1, 'C':2})
x1.to_csv(f'{path}/output.csv', index=False)
