# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:38:37 2018

@author: coolqeqe
"""

#libary 
import pandas as pd

#data import
data=pd.read_csv("veriler.csv")

#eksik veriler

#sklearn --> sci-kit learn
from sklearn.preprocessing import Imputer

imputer=Imputer(missing_values="NaN", strategy="mean", axis=0)

yas=data.iloc[:,1:4].values
print(yas)
imputer=imputer.fit(yas[:,1:4])
yas[:,1:4]=imputer.transform(yas[:,1:4])
print(yas)

