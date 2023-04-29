# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:56:22 2023

@author: Eilis.Donohue
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:44:36 2023

@author: Eilis.Donohue
"""
import os
import glob
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
# Setting the ticks on the x and y axis
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from numpy.polynomial import Polynomial as P
#import imgkit


def plot_histograms(data, var):   
        plt.figure()
        sns.histplot(data, x=var, hue="Class", binwidth=1, kde=True)
        plt.savefig(f'plots/histogram_{var}.png') 
        plt.close()
    
def get_corr(data):
    return data.corr()

def plot_rollingmean(data, window, iris, var, fig, axis):
    data['Rolling Mean'] = data[var].rolling(window).mean()
    data_np = data.to_numpy()
    # return the linear fit 
    linear_fit = get_linear_fit(data_np[:,0], data_np[:,2])
    x = np.linspace(np.min(data_np[:,0]), np.max(data_np[:,0]))                      
    y_fitted = linear_fit(x)
    data = pd.DataFrame(data_np, columns=["Index", var, "Rolling Mean"])
    data['Rolling_linear'] = y_fitted
    data['Mean'] = data[var].mean()
    data = data.drop(columns="Index").copy()
    axis.plot(data[var],'bo', linestyle='')
    axis.plot(data[['Rolling Mean', 'Rolling_linear', 'Mean']])   
    axis.set_ylabel(var +' (cm)')
    axis.set_xlabel('Sample Index')
   


def get_linear_fit(numpy_x, numpy_y):
    # return the indexes which have numbers in both x and y (to avoid nans)
    idx = np.isfinite(numpy_x) & np.isfinite(numpy_y)
    # Use the numpy polynomial fit method 
    linear_fit = P.fit(numpy_x[idx], numpy_y[idx], 1)
    return linear_fit


summary_filename = "summary/summary_statistics.txt"
corr_filename = "summary/correlation.txt"


# Read in the data from the source file - no header  
data = pd.read_csv('data/iris.data', header=None)
# Make a list of the columns
variables = ["Sepal Length", "Sepal Width", "Petal Length",
             "Petal Width", "Class"]
# List of variables without class
variables_wo_class = variables[:-1]
# Assign the header to the data
data.columns = variables

# get the different classifications
class_names = data["Class"].unique()
# dataframe without class column
data_wo_class = data.drop(columns="Class").copy()
data_wo_class_n = data_wo_class.to_numpy()    
# find size

iris_size = data_wo_class_n[:,0] * data_wo_class_n[:,1] + \
            data_wo_class_n[:,2] * data_wo_class_n[:,3]

#iris_size_df['Class'] = data['Class'] 
# find size
iris_size_df = pd.DataFrame(iris_size)
iris_size_df['Class'] = data['Class']
iris_size_df.columns = ('Size', 'Class')
#plot_histograms(iris_size_df, 'Size')
data['Size']= iris_size_df['Size']


setosa_data = data[data["Class"] == "Iris-setosa"].drop(columns = 'Class').copy()
virg_data = data[data["Class"] == "Iris-virginica"].drop(columns ='Class').copy()
vers_data = data[data["Class"] == "Iris-versicolor"].drop(columns ='Class').copy()


for iris in class_names:
     data_iris = data[data["Class"] == iris].drop(columns = 'Class').copy()
     fig, axs = plt.subplots(2, 2, figsize=(10, 10))
     axis_list = np.array([axs[0,0], axs[0,1], axs[1,0], axs[1,1]])
     for count, var in enumerate(variables_wo_class):         
         data_iris_variable = data_iris[var].reset_index()
         plot_rollingmean(data_iris_variable, 5, iris, var, fig, axis_list[count])
     fig.suptitle(iris, fontsize=16)
     axis_list[count].legend(['Measured','Rolling Mean', 'Rolling lin_fit', 'Mean'])
     plt.tight_layout()    
     fig.savefig(f'plots/rolling_mean_{iris}.png') 

for iris in class_names:
    fig, axs = plt.subplots(1)
    data_iris = data[data["Class"] == iris].drop(columns = 'Class').copy()
    data_iris_variable = data_iris['Size'].reset_index()
    plot_rollingmean(data_iris_variable, 5, iris, "Size", fig, axs)
    fig.suptitle(iris, fontsize=16)
    axs.legend(['Measured','Rolling Mean', 'Rolling lin_fit', 'Mean'])
    fig.savefig(f'plots/rolling_mean_size_{iris}.png')

#     plt.show()
        
        
#data_iris = data[data["Class"] == "Iris-setosa"].drop(columns = 'Class').copy()        
#data_iris_var = pd.DataFrame(data_iris['Sepal Length'])
#data_iris_var['Rolling Mean'] = data_iris_var.rolling(5).mean()
#data_iris_var.to_numpy()

#plt.figure()
#data_iris_var.plot()
#data_iris_var.plot()
#plt.savefig('plots/rolling_meantest.png')


#df_5sample_mean = setosa_data['Size'].resample(rule=5).mean()
#df_roll_mean6 = df_hour_means.rolling(6).mean()
#print(df_roll_mean6.head(10))
#df_roll_mean6.plot()
#df_hour_means.plot()


#first_digit = data_wo_class_str.str[0]