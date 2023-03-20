'''
PANDS Project 2023
Fischer's Iris Dataset
Author: Eilis Donohue
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math


sns.set_theme()
# Read in the data from the source file - no header  
data = pd.read_csv('data\iris.data', header=None)
# List the column/variable names
columns = ["Sepal Length", "Sepal Width", "Petal Length",\
           "Petal Width", "Class"]

# Assign a header to the data
data.columns = columns

#summary = data.describe()

class_names = data["Class"].unique()
# Slice the dataframe to separate the Iris classes into separate dataframes
# containing only the measurement data
iseto = data[data["Class"] == "Iris-setosa"].iloc[:, 0:4]
ivers = data[data["Class"] == "Iris-versicolor"].iloc[:, 0:4]
ivirg = data[data["Class"] == "Iris-verginica"].iloc[:, 0:4]


def summary_stats(data, vars, filename='summary/variable_summary.txt'):
    # Get some overall basic stats on the whole dataset
    all_min = data.min()
    all_max = data.max() 
    all_mean = data.mean()
    all_median = data.median()
    all_stdev = data.std()
    # Write some summary files for the basic stats
    with open (filename, 'wt') as f:
        f.write(f'Variable, Min (cm), Max (cm), Mean (cm), Median(cm), Standard Deviation (cm)\n')
        for var in vars:           
            f.write(f'{var}, {round(all_min[var], 4)}, {round(all_max[var],4) }, ')
            f.write(f'{round(all_mean[var],4)}, {round(all_median[var],4)}, {round(all_stdev[var],4)}\n')
        



# call summary_stats to write a file which summarises the data
summary_stats(data, columns[:-1])



#sns.relplot(data=iseto, x="Sepal Length", y="Sepal Width")
#test_hist = iseto.hist(column="Sepal Length")
#print(test_hist)
# subset of the data for testing plots
small_data = data.iloc[0:5, :]
#print(small_data)

#sns.pairplot(data=data, hue="Class")

#plt.savefig("plots/pairplot.png")

#sns.displot(data=data, x="Petal Length", col="Class", kde=True)
#plt.savefig("plots/displot.png")

min_petallength = data["Petal Length"].min()
all_min = data.min() 
all_max = data.max()
bin_size = 0.2
#print(all_min, min_petallength)

min_PL = all_min["Petal Length"]
print("ALL MIN", all_min)
print("min_PL", min_PL)

bins = np.arange(math.floor(all_min["Petal Length"]), math.ceil(all_max["Petal Length"])+1, bin_size)
#print(min_data)

sns.histplot(data=data, x="Petal Length", hue="Class", bins=bins, kde=True)
plt.savefig("plots/histplot.png")            

def describe_df(df, class_item):
    return data[data["Class"] == class_item].describe()
    



#for item in class_names:
#    summary = describe_df(data, item)
 #   summary.to_csv(item +'.txt')




#print(iseto)
#sepal_width_mean = data["Sepal Width"].mean()
#print(data.count(axis=0))
#data.mean()
#print(data)