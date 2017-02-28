# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import numpy
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 

#load csv file
data = pandas.read_csv('GapMinder_mine.csv', low_memory=False)
#Replace all blank spaces in file with NAN
data = data.apply(lambda x: x.str.strip()).replace('', numpy.nan)

#To ensure data is in numeric format
data['co2emissions'] = data['co2emissions'].convert_objects(convert_numeric=True)
data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True)

#function to find class interval of W=UrbanRate and LifeExpectancy
def create_New_Varable_For_Urban_Or_Life(urbanORlife):
   if (urbanORlife >0) & (urbanORlife <=20):
       return 1
   elif(urbanORlife >20) & (urbanORlife <=40):
       return 2    
   elif(urbanORlife >40) & (urbanORlife <=60):
       return 3        
   elif(urbanORlife >60) & (urbanORlife <=80):
       return 4
   elif(urbanORlife >80) & (urbanORlife <=100):
       return 5

sub1=data[(data['urbanrate']>=0) & (data['lifeexpectancy']>=0)]

#Calls the function created to find class interval
sub1['Urbanrate_new']= sub1['urbanrate'].apply(create_New_Varable_For_Urban_Or_Life)
sub2 = sub1[['Urbanrate_new', 'lifeexpectancy']].dropna()

# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='lifeexpectancy ~ C(Urbanrate_new)', data=sub2)
results1 = model1.fit()
print (results1.summary())


print ('means for lifeexpectancy by Urban Rate')
m1= sub2.groupby('Urbanrate_new').mean()
print (m1)

print ('standard deviations for lifeexpectancy by Urban Rate')
sd1 = sub2.groupby('Urbanrate_new').std()
print (sd1)


mc1 = multi.MultiComparison(sub2['lifeexpectancy'], sub2['Urbanrate_new'])
res1 = mc1.tukeyhsd()
print(res1.summary())