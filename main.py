
import pandas as pd
import numpy as np
# x = [23, 48, 19]
# my_first_series = pd.Series(x)
# print(my_first_series)

# data = {
#     "students": ['Emma', 'John', 'Bob'],
#     "grades": [12, 18, 17]
# }
# # my_first_dataframe = pd.DataFrame(data)
# # print(my_first_dataframe)
#
# my_first_df=  pd.DataFrame(data)
# print(my_first_df['students'])

# data = {
#     "students": ['Emma', 'John', np.nan, 'Bob'],
#     "grades": [12, np.nan, 18, 17]
# }
# my_first_df = pd.DataFrame(data, index=["a", "b", "c","d"])
# print(my_first_df.isnull())

# data = {
#     "students": ['Emma', 'John', np.nan, 'Bob'],
#     "grades": [12, np.nan,18, 17]
# }
# my_first_df = pd.DataFrame(data, index=["a", "b", "c", "d"])
# df2 = my_first_df.replace(to_replace="Bob", value="Alice")
# print(df2)

# data = {
#     "students": ['Emma', 'John', 'Mary', 'Bob'],
#     "grades": [12, np.nan,18, np.nan]
# }
# my_first_df=  pd.DataFrame(data, index=["a", "b", "c", "d"])
# df = my_first_df.interpolate(method='linear', limit_direction='forward')
# print(df)

# data = {
#     "students": ['Emma', 'John', 'Mary', 'Bob'],
#     "grades": [12, np.nan,18, np.nan]
# }
# my_first_d = pd.DataFrame(data, index=["a", "b", "c", "d"])
# my_first_d.dropna(inplace=True)
# print(my_first_d)

# s = pd.Series(['workearly', 'e-learning', 'python'])
# print(s)
# for index, value in s.items():
#     print(f"Index : {index}, Value : {value}")

# data = {
#     "students": ['Emma', 'John'],
#      "grades": [12, 19.8]
# }
# my_first_df = pd.DataFrame(data, index=["a", "b"])
# for i, j in my_first_df.iterrows():
#       print(i, j)
#       print()

# data = {
#     "students": ['Emma', 'John'],
#      "grades": [12, 19.8]
# }
# my_first_df = pd.DataFrame(data, index=["a", "b"])
# columns = list(my_first_df)
# for i in columns:
#       print(my_first_df[i][1])

# df = pd.read_csv("finance_liquor_sales.csv")
# print(df.head())
# print(df.tail())
# print(df.info())

# mean = df.mean(numeric_only=True)
# print(mean)
# median = df.median(numeric_only=True)
# print(median)
#
# max_v = df.max(numeric_only=True)
# print(max_v)
# summary = df.describe()
# print(summary)
#
# df = pd.read_csv("finance_liquor_sales.csv")
# cn = df.groupby('category_name')
# print(cn.first())

# df = pd.read_csv("finance_liquor_sales.csv")
# cnc = df.groupby(['category_name', 'city'])
# print(cnc.first())

# df = pd.read_csv("finance_liquor_sales.csv")
# cn = df.groupby('category_name')
# print(cn.aggregate(np.sum))

#
# df = pd.read_csv("finance_liquor_sales.csv")
# cn2 = df.groupby(['category_name', 'city'])
# print(cn2.agg({'bottles_sold': 'sum', 'sale_dollars': 'mean'}))


# df = pd.read_csv("finance_liquor_sales.csv")
# ng = df.groupby('vendor_name')
# print(ng.filter(lambda x: len(x) >= 20))

# d1 = {'Name': ['Mary', 'John', 'Alice', 'Bob'],
#          'Age': [27, 24, 22, 32],
#          'Position': ['Data Analyst', 'Trainee', 'QA Tester', 'IT']}
# d2 = {'Name': ['Steve', 'Tom', 'Jenny', 'Nick'],
#           'Age': [37, 25, 24, 52],
#           'Position': ['IT', 'Data Analyst', 'Consultant', 'IT']}
# df1 = pd.DataFrame(d1, index=[0, 1, 2, 3])
# df2 = pd.DataFrame(d2, index=[4, 5, 6, 7])
# result = pd.concat([df1, df2])
# print(result)

# d1 = {'key': ['a', 'b', 'c', 'd'],
#       'Name': ['Mary', 'John', 'Alice', 'Bob']}
# d2 = {'key': ['a', 'b', 'c', 'd'],
#       'Age': [27, 24, 22, 32]}
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# result = pd.merge(df1, df2, on='key')
# print(result)

# d1 = {'Name': ['Mary', 'John', 'Alice', 'Bob'],
#       'Age': [27, 24, 42, 32]}
# d2 = {'Position': ['Data Analyst', 'Trainee', 'QA Tester', 'IT'],
#       'Years_of_experience':[5, 1, 10, 3] }
# df1 = pd.DataFrame(d1, index=[0, 1, 2, 3])
# df2 = pd.DataFrame(d2, index=[0, 2, 3, 4])
# result = df1.join(df2, how='inner')
# print(result)

# d = {'col1': [1, 2, 3, 4, 7, 11],
#        'col2': [4, 5, 6, 9, 5, 0],
#        'col3': [7, 5, 8, 12, 1,11]}
# df = pd.DataFrame(d)
# print(df)
# print()
# s1 = df.iloc[:, 0]
# print("1st column as a Series:")
# print(s1)
# print(type(s1))

# df = pd.read_csv('data.csv')
# # print(df.head(20))
# for i, j in df.iterrows():
#    print(i, j)

# data = pd.read_csv('1.supermarket.csv')
# # print(data.head())
# # print('\nShape of dataset: ', data.shape)
# # print(data.info())
# print(data.columns)
# x=data.groupby('item_name')
# x=x.sum()
# print(x.head(1))

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_txt = requests.get(url).text
s = BeautifulSoup(url_txt, "html.parser")
print(s.prettify())