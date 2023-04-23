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

#import imgkit

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


fig=plt.figure()
#plt.gcf().subplots_adjust(top=0.8)
df1 = data[data["Class"] == "Iris-setosa"].drop(columns = "Class").copy()
df2 = data[data["Class"] == "Iris-versicolor"].drop(columns = "Class").copy()
fig, ax = plt.subplots(nrows = 2, ncols =2, figsize=(10,8))

#for i, var_name in enumerate(variables_wo_class):
#    fig, ax = fig.add_subplot(2,2,i+1)
sns.histplot(data, x="Petal Length", hue="Class", binwidth=0.2, kde=True, ax=ax[0,0])
sns.histplot(data, x="Petal Width", hue="Class", binwidth=0.2, kde=True, ax=ax[0,1])
sns.histplot(data, x="Sepal Length", hue="Class", binwidth=0.2, kde=True, ax=ax[1,0])
sns.histplot(data, x="Sepal Width", hue="Class", binwidth=0.2, kde=True, ax=ax[1,1])



fig.tight_layout()

plt.show()
#    plt.hist([df1, df2], bins=10, label=['x', 'y'])
  #  df1.hist(bins=10,ax=ax)
 #   df2.hist(bins=10, ax=ax)   
#    plt.title(var_name)

#sns.move_legend(
 #   fig, "upper left",
 #   bbox_to_anchor=(0.5, 1), ncol=3, title=None, frameon=False,)

# add legend
#handles, labels = ax.get_legend_handles_labels()
#plt.gcf().legend

    
    
    

    # fig=plt.figure()
    # for i, var_name in enumerate(variables):
    #     ax=fig.add_subplot(n_rows,n_cols,i+1)
    #     df[var_name].hist(bins=10,ax=ax)
    #     ax.set_title(var_name+" Distribution")
    # fig.tight_layout()  # Improves appearance a bit.
    # plt.show()