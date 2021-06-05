# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:17:07 2021

@author: smrvr
"""
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dicts = {"Countries":['India','Canada','USA','UK','Japan', 'Indonesia'],
              "Volume_in_ML":[2,1,1.5,1.9,2,1],
              "Amount_in_BL":[3,2.5,5,6,1,12],
              "Population":[1.3,0.035,0.3,0.05,0.1,0.27]}

Cards = pd.DataFrame(dicts)

Cards


plt.plot(Cards['Countries'],Cards[['Volume_in_ML']]
         ,marker='o',linewidth=5,markersize=10
         ,markerfacecolor='white',markeredgecolor='black'
         ,linestyle='dashed'
         ,color='red')
plt.plot(Cards['Countries'],Cards[['Amount_in_BL']]
         ,marker='o',linewidth=5,markersize=10
         ,markerfacecolor='white',markeredgecolor='black'
         ,linestyle='dashed'
         ,color='blue')
plt.plot(Cards['Countries'],Cards[['Population']]
         ,marker='o',linewidth=5,markersize=10
         ,markerfacecolor='white',markeredgecolor='black'
         ,linestyle='dashed'
         ,color='green')
plt.legend(['Volume_in_ML','Amount_in_BL','Population'])
plt.grid()
plt.xlabel('Countries')
plt.ylabel('Values')
plt.title('Cards information')
plt.tight_layout()






