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


iris = datasets.load_iris()
iris_data_scikit= iris.data

iris_scikit = pd.DataFrame(iris.data)
iris_scikit.columns = iris.feature_names

iris_scikit['Class'] = iris.target

ref_dict = {}
ref_dict.keys = iris.target_names()

for i, row in enumerate(iris.target_names.tolist()):
    ref_dict[i] = "Iris-"+row

iris_scikit['Class'].replace(ref_dict)




