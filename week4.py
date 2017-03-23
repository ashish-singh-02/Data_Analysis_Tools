# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:42:02 2017

@author: Ashish
"""

import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

#load csv file
data = pandas.read_csv('GapMinder_mine.csv', low_memory=False)
#Replace all blank spaces in file with NAN
data = data.apply(lambda x: x.str.strip()).replace('', numpy.nan)

data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True)
data['incomeperperson'] = data['incomeperperson'].convert_objects(convert_numeric=True)

data_clean=data.dropna()

def incomegrp (row):
   if row['incomeperperson'] <= 744.239:
      return 1
   elif row['incomeperperson'] <= 9425.326 :
      return 2
   elif row['incomeperperson'] > 9425.326:
      return 3
   
data_clean['incomegrp'] = data_clean.apply (lambda row: incomegrp (row),axis=1)

chk1 = data_clean['incomegrp'].value_counts(sort=False, dropna=False)
print(chk1)

sub1=data_clean[(data_clean['incomegrp']== 1)]
sub2=data_clean[(data_clean['incomegrp']== 2)]
sub3=data_clean[(data_clean['incomegrp']== 3)]

print ('####association between urbanrate and Life Expectancy for LOW income countries####')
print (scipy.stats.pearsonr(sub1['urbanrate'], sub1['lifeexpectancy']))
print ('       ')
print ('####association between urbanrate and internetuserate for MIDDLE income countries####')
print (scipy.stats.pearsonr(sub2['urbanrate'], sub2['lifeexpectancy']))
print ('       ')
print ('####association between urbanrate and internetuserate for HIGH income countries####')
print (scipy.stats.pearsonr(sub3['urbanrate'], sub3['lifeexpectancy']))

scat1 = seaborn.regplot(x="urbanrate", y="lifeexpectancy", data=sub1)
plt.xlabel('Urban Rate')
plt.ylabel('Life Expectancy')
plt.title('####Scatterplot for the Association Between Urban Rate and Life Expectancy for LOW income countries####')
print (scat1)
#%%
scat2 = seaborn.regplot(x="urbanrate", y="lifeexpectancy", fit_reg=False, data=sub2)
plt.xlabel('Urban Rate')
plt.ylabel('Life Expectancy')
plt.title('####Scatterplot for the Association Between Urban Rate and Life Expectancy for MIDDLE income countries####')
print (scat2)
#%%
scat3 = seaborn.regplot(x="urbanrate", y="lifeexpectancy", data=sub3)
plt.xlabel('Urban Rate')
plt.ylabel('Life Expectancy')
plt.title('####Scatterplot for the Association Between Urban Rate and Life Expectancy for HIGH income countries####')
print (scat3)
