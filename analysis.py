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

#for item in class_names:
#    df_corr.concat(get_corr(iris_data))


# ****************************** Plotting ************************************      
# Generate the pair plot of scatters
sns.set_theme()
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

plt.figure()
g = sns.scatterplot(data=data, x="Petal Width", y="Petal Length", hue="Class")
#ax = g.axes
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles=handles[1:], labels=labels[1:])

plt.savefig("plots/petal_scatter.png")

#g = sns.relplot(data=data, x="Sepal Width", y="Sepal Length", hue="Class")
#g.savefig("plots/sepal_scatter.png")


#test_hist = iseto.hist(column="Sepal Length")
#print(test_hist)
# subset of the data for testing plots
small_data = data.iloc[0:5, :]
#print(small_data)


#sns.displot(data=data, x="Petal Length", col="Class", kde=True)
#plt.savefig("plots/displot.png")

min_petallength = data["Petal Length"].min()
all_min = data.min() 
all_max = data.max()
bin_size = 0.2
#print(all_min, min_petallength)

min_PL = all_min["Petal Length"]
#print("ALL MIN", all_min)
#print("min_PL", min_PL)

#bins = np.arange(math.floor(all_min["Petal Length"]), math.ceil(all_max["Petal Length"])+1, bin_size)
#print(min_data)

#sns.histplot(data=data, x="Petal Length", hue="Class", bins=bins, kde=True)
#plt.savefig("plots/histplot.png")            

    #def main():


#if __name__ == "__main__":
#    main()



