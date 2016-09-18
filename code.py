# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 19:48:09 2016

@author: ABC
"""

import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel('D:\KULIAH\Materi\Visualisasi Data\Bubble Plot Map\data.xlsx')
fig = plt.figure(figsize=(10,8))

ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Bonus')
ax.set_ylabel('Base Salary')
ax.scatter(data['Bonus'],data['Base Salary'], s=data['Size'], c=data['No'] )
for i,text in enumerate(data['Job Title']):
    ax.annotate(text,(data['Bonus'][i],data['Base Salary'][i]))

plt.show()