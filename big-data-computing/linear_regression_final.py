# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:45:55 2019

@author: Anirudh Bellamkonda
"""

import numpy as np 
import matplotlib.pyplot as plt

# Problem data
month_data      =   np.array([3,5,7,9,12,15,18]) 
profit_data     =   np.array([100,250,330,590,660,780,890])

total_data_points   =   np.size(month_data) 
  
# Mean of month_data and profit_data
mean_month      =   np.mean(month_data)
mean_profit     =   np.mean(profit_data) 
  
# Calculating cross-deviation and deviation
SS_xy = np.sum(profit_data*month_data) - total_data_points*mean_profit*mean_month 
SS_xx = np.sum(month_data*month_data) - total_data_points*mean_month*mean_month 
  
# calculating regression coefficients 
beta = SS_xy / SS_xx 
alpha = mean_profit - beta*mean_month

# calculating notes coefficients
sum_x = np.sum(month_data)
print("sum_x: ",sum_x)
sum_y = np.sum(profit_data)
print("sum_y: ",sum_y)
sum_xy = np.dot(month_data,profit_data)
print("sum_xy: ",sum_xy)
sum_x_square = np.square(sum_x)
print("sum_x_square: ",sum_x_square)

# Estimating the coefficients 
print("Coefficient:\nalpha\t:\t{}  \nbeta\t:\t{}".format(alpha, beta))


p_next_year = alpha+beta*30;
print("Expected rate of profit over next year: {}".format(p_next_year))

# plotting regression line 
# plotting the actual points as scatter plot 
plt.scatter(month_data, profit_data, color = "r", marker = "o", s = 30) 
  
# predicted response vector 
y_pred = alpha + beta*month_data
  
# plotting the regression line 
plt.plot(month_data, y_pred, color = "b") 
  
# Setting lable names for the plot
plt.xlabel('Months') 
plt.ylabel('Profit (in K$, 1K=1000$)') 
  
# Plotiing the graph
plt.show() 