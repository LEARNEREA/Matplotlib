# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:12:48 2021

@author: smrvr
"""
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt


dicts = {"Years":[2015,2016,2017,2018,2019,2020],
              "Cards":[2,1,1.5,1.9,2,1],
              "Mortgage":[3,2.5,5,6,1,12],
              "VAF":[1.3,0.035,0.3,0.05,0.1,0.27]}
prod = pd.DataFrame(dicts)
prod

plt.stackplot(prod['Years'],prod['Cards'],prod['Mortgage'],prod['VAF']
              ,colors=('red','green','blue')
              ,baseline='sym'
              )
plt.legend(['Cards','Mortgage','VAF'],loc='upper left')
plt.grid()

