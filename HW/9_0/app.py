"""
Дан файл california_housing_train.csv. Определить среднюю стоимость дома ,
где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
"""




import pandas as pd


df = pd.read_csv('HW/9_0/california_housing_train.csv')

res = df[(df['population'] < 500) & (df['population'] > 0)]
avg = res['median_house_value'.mean()]
