# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:02:44 2023

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
from sklearn import datasets
#from PIL import Image
#from pytesseract import pytesseract


summary_filename = "summary/summary_statistics.txt"
corr_filename = "summary/correlation.txt"


# Read in the data from the source file - no header  
data = pd.read_csv('data/iris.data', header=None)
data2 = pd.read_csv('data/bezdekIris.data', header=None)
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


fig, axs = plt.subplots(1, 3, figsize=(20, 8))
axs[0].set_ylabel('Measurement (cm)')

for ax, iris in enumerate(class_names):
    
    data_iris = data[data["Class"] == iris].drop(columns = 'Class').copy()
    print(data_iris.describe())
    #fig = plt.figure(figsize=(4,8))
    axs[ax].set_ylim(0, 8)
    axs[ax].boxplot(data_iris, labels=variables_wo_class)
    axs[ax].set_title(iris)
    
plt.savefig('data_plots/boxplot_classes.png', bbox_inches='tight')   
plt.show()
#     fig, axs = plt.subplots(2, 2, figsize=(10, 10))
#     axis_list = np.array([axs[0,0], axs[0,1], axs[1,0], axs[1,1]])
#     for count, var in enumerate(variables_wo_class):         
#         data_iris_variable = data_iris[var].reset_index()
#         plot_rollingmean(data_iris_variable, 5, iris, var, fig, axis_list[count])
#     fig.suptitle(iris, fontsize=16)
#     axis_list[count].legend(['Measured','Rolling Mean', 'Rolling lin_fit', 'Mean'])
#     plt.tight_layout()    
#plt.savefig(f'{plots_folder}line_RollingMean_{iris}.png')   

