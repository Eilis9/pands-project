'''
PANDS Project 2023
Fisher's Iris Dataset
Author: Eilis Donohue (G00006088)
'''
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

summary_filename = "summary/summary_statistics.txt"
corr_filename = "summary/correlation.txt"

# ************************ Function definitions ***************************
# Function to calculate the basic statistics of a dataset
def get_summary_stats(data, item=''):
    # Get the basic stats 
    summary_df = pd.DataFrame()
    summary_df['Min (cm)'] = data.min()
    summary_df['Max (cm)'] = data.max()
    summary_df['Mean (cm)'] = data.mean()
    summary_df['Median (cm)'] = data.median()
    summary_df['StDev (cm)'] = data.std()
    summary_df['Variance (cm)'] = data.var() 
    
    return summary_df

# Function to write a summary of data to a file 
def write_to_file(summary_filename, df_data, heading, dec_format="%.2f"):   
    with open (summary_filename, 'at') as f:
        # to_string for nice formatting for the text file
        df_summary_asstr = df_data.to_string(float_format=dec_format, 
                                                justify='center')
        # write header and data 
        f.write(f'***************** {heading} *****************\n')
        f.write(f'{df_summary_asstr}\n')
        f.write('\n')

# Function to plot histograms of data 
def plot_histograms(data, var):   
        plt.figure()
        sns.histplot(data, x=var, hue="Class", binwidth=0.2, kde=True)
        plt.savefig(f'plots/histogram_{var}.png')  

# Run pandas correlation method
def get_corr(data):
    return data.corr()

# Function to get a linear regression fit between 2 numpy arrays
def get_linear_fit(numpy_x, numpy_y):
    # return the indexes which have numbers in both x and y (to avoid nans)
    idx = np.isfinite(numpy_x) & np.isfinite(numpy_y)
    # Use the numpy polynomial fit method 
    linear_fit = P.fit(numpy_x[idx], numpy_y[idx], 1)
    return linear_fit

def plot_rollingmean(data, window, iris, var, axis, fig):
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
  
# ***************************** Reading in data ******************************
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
print("Data read in")

# ********************** Outputting the summary stats ************************
# Delete anything in summary directory
files = glob.glob('summary/*')
for f in files:
    os.remove(f)
    
# Get the statistics for the whole dataset and write to file
df_summary_all = get_summary_stats(data.drop(columns="Class"))
write_to_file(summary_filename, df_summary_all, "All data")
df_corr_all = get_corr(data)
write_to_file(corr_filename, df_corr_all, "All data", "%.3f")

# Get summary stats and corr for each class of iris and write to text file
for item in class_names:
    # Extract the data related to one class of iris
    iris_data = data[data["Class"] == item].copy()
    # Strip the class column before passing to function
    iris_data.drop(columns = "Class", inplace=True) 
    # Get the stats and write to file
    df_summary = get_summary_stats(iris_data)
    write_to_file(summary_filename, df_summary, item)
    df_corr =  get_corr(iris_data)
    write_to_file(corr_filename, df_corr, item, "%.2f")   

# Pandas dataframe of correlation stats
df_corr = pd.DataFrame()
df_corr = get_corr(data_wo_class)
#df_corr_plot.lock(["SL-SW"]["All"]) = df_corr.loc(index="Sepal Length", columns="Sepal Width")
print(f"Summary stats in {summary_filename} and {corr_filename}")


#for item in class_names:
#    df_corr.concat(get_corr(iris_data))


# ****************************** Plotting ************************************      
# Generate the pair plot of scatters
sns.set_theme(style='whitegrid')
g = sns.pairplot(data, hue="Class", diag_kind="kde")
g.map_lower(sns.kdeplot, levels=7, color=".2")
g.savefig("plots/pairplot.png")

# Generate the histograms for the 4 iris measurement variables
for var in variables_wo_class:
    plot_histograms(data, var)   
    
# Plot histogram for the full dataset    
plt.figure()
sns.histplot(data_wo_class, binwidth=0.2, kde=True)
plt.savefig('plots/histogram_all_data.png')  

custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", )

# Plot Petal Width v Petal Length
plt.figure()
g = sns.scatterplot(data=data, x="Petal Width", y="Petal Length", hue="Class")
plt.savefig("plots/petal_scatter.png")

# Plot Sepal Length v Sepal Width
plt.figure()
g = sns.scatterplot(data=data, x="Sepal Width", y="Sepal Length", hue="Class")
plt.savefig("plots/sepal_scatter.png")

# Create a figure with 4 histogram subplots showing each variable
sns.set_theme(style='white')
fig, ax = plt.subplots(nrows = 2, ncols =2, figsize=(10,8))
sns.histplot(data, x="Petal Length", hue="Class", binwidth=0.2, kde=True, ax=ax[0,0])
sns.histplot(data, x="Petal Width", hue="Class", binwidth=0.2, kde=True, ax=ax[0,1])
sns.histplot(data, x="Sepal Length", hue="Class", binwidth=0.2, kde=True, ax=ax[1,0])
sns.histplot(data, x="Sepal Width", hue="Class", binwidth=0.2, kde=True, ax=ax[1,1])
fig.tight_layout()
plt.savefig("plots/4_plot_histogram.png")
print("Plots in /plots")

# ******************************* Other Analysis *****************************
# For each iris type, create a plot with 4 subplots of the measurements with 
#a rolling mean  calculated, a linear fit of that rolling mean and also 
#the mean of the dataset. 
for iris in class_names:
     data_iris = data[data["Class"] == iris].drop(columns = 'Class').copy()
     fig, axs = plt.subplots(2, 2, figsize=(10, 10))
     axis_list = np.array([axs[0,0], axs[0,1], axs[1,0], axs[1,1]])
     for count, var in enumerate(variables_wo_class):         
         data_iris_variable = data_iris[var].reset_index()
         plot_rollingmean(data_iris_variable, 5, iris, var, axis_list[count], fig)
     fig.suptitle(iris, fontsize=16)
     axis_list[count].legend(['Measured','Rolling Mean', 'Rolling_linear', 'Mean'])
     plt.tight_layout()    
     fig.savefig(f'plots/rolling_mean_{iris}.png') 



#first_digit = data_wo_class_str.str[0]
 

