# import opendatasets as od 
# token = {"username":"alex409","key":"5630cbbacdcd758e0a3ff6bfd20a1ca6"}
# od.download("https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/") 

import pandas as pd
import os
# import matplotlib.pyplot as plt

# для загрузки файлов (*.csv) из папки скрипта
# Получение пути к текущему скрипту
script_path = os.path.dirname(os.path.realpath(__file__))

# Изменение текущей директории на директорию скрипта
os.chdir(script_path)

import pandas as pd # библиотека для работы с данными 
import fastai # библиотека для работы с нейронными сетями 
from fastai.tabular.all import* # блок для связки нейронных сетей и табличных данных
train_data = pd.read_csv("./house-prices-advanced-regression-techniques/train.csv")
train_data = train_data.drop("Id", axis = 1)
print(train_data.head()) 
print(train_data.dtypes)

c=[]
n=[]
for i in train_data.columns:
    if(train_data[i].dtype) in ['object']:
        c.append(i) 
stay=["MSSubClass", "OverallQual", "OverallCond", "YearBuilt", "YearRemodAdd", "SalePrice"]

for i in train_data.columns:
    if i not in stay and i not in c:
        n.append(i)
    
print(train_data[c].info())
print(train_data[n].info())

print(len(c), len(n))

print(train_data.info())