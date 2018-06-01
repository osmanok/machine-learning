# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:38:37 2018

@author: coolqeqe
"""

#libary 
import pandas as pd
import numpy as np

#data import

data=pd.read_csv("veriler.csv")

print(data)


boy=data[["boy"]]
print(boy)

boykilo=data[["boy","kilo"]]
print(boykilo)

class human:
    boy=180;
    def run(self , b):
        return b+10
    
ali=human()
print(ali.boy)
print(ali.run(90))