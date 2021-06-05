# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:16:27 2021

@author: smrvr
"""

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets as df
import pandas as pd

pd.set_option('max_columns',None)

#Importing default boston data and creating a pandas dataframe
boston=pd.DataFrame(df.load_boston().data,columns=(df.load_boston().feature_names))
boston.head()
boston.columns

boston.info()

plt.hist(boston['AGE'],edgecolor='black',bins=[0,25,50,75,100],color='green')
plt.xticks([0,25,50,75,100])
plt.xlabel('Age Intervals')
plt.ylabel('Counts')
plt.title('Age Distribution')

columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']

#Automatically create a separate Hostogram for each of the variable in Boston dataframe
for i in columns:
    plt.hist(boston[i])
    plt.title(i)
    plt.show()


