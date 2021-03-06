# -*- coding: utf-8 -*-
"""anova.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zc1bownrzDBfml9XXcWtrUy9sWaCk8ib
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm


'''
from google.colab import files
uploaded = files.upload()
'''


#anova test
#problem: which web frameworks do experienced programmers are desiring next year
#         among django, asp.net and angular
#null hypothesis: all the webframeworks are equally desired
#alternative: all the webframeworks are not equally desired



data = pd.read_csv('survey_results_public.csv')
data = data.replace('NA', np.nan) #replace empty cells with np.null

framework_desired_node = data['WebframeDesireNextYear'].str.contains('React.js', na=False) #columns containing asp.net will be selected
print(framework_desired_node.head())
years_node = data[framework_desired_node]['YearsCode'] #how many years the person is  coding

framework_desired_angular = data['WebframeDesireNextYear'].str.contains('Angular', na=False) #columns containing C# will be selected
years_angular = data[framework_desired_angular]['YearsCode'] #how many years the c# user is coding

framework_desired_net = data['WebframeDesireNextYear'].str.contains('ASP.NET', na=False) #columns containing C# will be selected
years_net = data[framework_desired_net]['YearsCode'] #how many years the c# user is coding

years_node = years_node.dropna()
years_angular = years_angular.dropna()
years_net = years_net.dropna()

years_node = years_node.replace('Less than 1 year', .5)
years_node = years_node.replace('More than 50 years', 55)

years_angular = years_angular.replace('Less than 1 year', .5)
years_angular = years_angular.replace('More than 50 years', 55)

years_net = years_net.replace('Less than 1 year', .5)
years_net = years_net.replace('More than 50 years', 55)

years_node = pd.to_numeric(years_node)
years_net = pd.to_numeric(years_net)
years_angular = pd.to_numeric(years_angular)

years_node = years_node[years_node > 0]
years_net = years_net[years_net > 0]
years_angular = years_angular[years_angular > 0]


print(years_node.describe())
print(years_node.median())
print(years_node.mode())

print(years_net.describe())
print(years_net.median())
print(years_net.mode())

print(years_angular.describe())
print(years_angular.median())
print(years_angular.mode())


result = stats.levene(years_node, years_net, years_angular) #equal variance test
w, pvalue = stats.bartlett(years_node, years_net, years_angular) #equal variance test
print(result)
print(pvalue)
#if pvalue is less than .05 then variances are not homogenous

sm.qqplot(np.log(years_node), line='r') #normality test
sm.qqplot(np.log(years_angular), line='r') #normality test
sm.qqplot(np.log(years_net), line='r') #normality test

F, p = stats.f_oneway(years_node, years_net, years_angular)
# Seeing if the overall model is significant
print('F-Statistic = %.3f, p = %.3f' % (F, p))
#if p is less then .05 we will reject null hypothesis


  