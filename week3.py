#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:28:43 2017

@author: ashish
"""


import pandas
import numpy
import scipy
import matplotlib.pyplot as plt
import seaborn

#load csv file
data = pandas.read_csv('GapMinder_mine.csv', low_memory=False)
#Replace all blank spaces in file with NAN
data = data.apply(lambda x: x.str.strip()).replace('', numpy.nan)

#To ensure data is in numeric format
data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True)

data_clean=data.dropna()

print ('##########Association between urbanrate and lifeexpectancy###########')
print(scipy.stats.pearsonr(data_clean['urbanrate'], data_clean['lifeexpectancy']))

#Scatterplot to verify linear relationship.
scat1 = seaborn.regplot(x='urbanrate', y='lifeexpectancy', fit_reg=True, data=data)
plt.xlabel('Urban Rate')
plt.ylabel('Life Expectancy Rate')
plt.title('Scatterplot for the Association Between Urban Rate and Life Expectancy')
