# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas
import numpy
import scipy.stats

#load csv file
data = pandas.read_csv('GapMinder_mine.csv', low_memory=False)
#Replace all blank spaces in file with NAN
data = data.apply(lambda x: x.str.strip()).replace('', numpy.nan)

# new code setting variables you will be working with to numeric
data['lifeexpectancy'] = pandas.to_numeric(data['lifeexpectancy'], errors='coerce')
data['urbanrate'] = pandas.to_numeric(data['urbanrate'], errors='coerce')

#function to find class interval of UrbanRate and LifeExpectancy
def create_New_Varable_For_Urban(urban):
   if (urban >0) & (urban <=50):
       return 1
   elif(urban >50) & (urban <=100):
       return 2

#function to find class interval of UrbanRate and LifeExpectancy
def create_New_Varable_For_Life(life):
   if (life >0) & (life <=20):
       return 1
   elif(life >20) & (life <=40):
       return 2    
   elif(life >40) & (life <=60):
       return 3        
   elif(life >60) & (life <=80):
       return 4
   elif(life >80) & (life <=100):
       return 5
   

sub1=data[(data['lifeexpectancy']>=0) & (data['urbanrate']<=100)]
sub1['urbanrate_new']= sub1['urbanrate'].apply(create_New_Varable_For_Urban)
sub1['Lifeexpectancy_new']= sub1['lifeexpectancy'].apply(create_New_Varable_For_Life)
# contingency table of observed counts
ct1=pandas.crosstab(sub1['urbanrate_new'], sub1['Lifeexpectancy_new'])
print (ct1)

# column percentages
colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)

# chi-square
print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)


recode2 = {4: 4, 3: 3}
sub1['COMP1v2']= sub1['Lifeexpectancy_new'].map(recode2)

# contingency table of observed counts
ct2=pandas.crosstab(sub1['urbanrate_new'], sub1['COMP1v2'])
print (ct2)

# column percentages
colsum2=ct2.sum(axis=0)
colpct2=ct2/colsum2
print(colpct2)

print ('chi-square value, p value, expected counts')
cs2= scipy.stats.chi2_contingency(ct2)
print (cs2)

recode3 = {5: 5, 4:4}
sub1['COMP3']= sub1['Lifeexpectancy_new'].map(recode3)

# contingency table of observed counts
ct3=pandas.crosstab(sub1['urbanrate_new'], sub1['COMP3'])
print (ct3)

# column percentages
colsum3=ct3.sum(axis=0)
colpct3=ct3/colsum3
print(colpct3)

print ('chi-square value, p value, expected counts')
cs3= scipy.stats.chi2_contingency(ct3)
print (cs3)