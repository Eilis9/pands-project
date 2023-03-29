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



def summary_stats(data, vari, filename='summary/variable_summary.txt'):
    # Get some overall basic stats on the whole dataset
    all_min = data.min()
    all_max = data.max() 
    all_mean = data.mean()
    all_median = data.median()
    all_stdev = data.std()
    # Write some summary files for the basic stats
    with open (filename, 'wt') as f:
        # Write file header
        f.write(f'Variable, Min (cm), Max (cm), Mean (cm), Median(cm), Standard Deviation (cm)\n')
        # for each variable write a new line
        for var in vari:           
            f.write(f'{str(var).ljust(20)}){str(round(all_min[var], 4)).rjust(20)}, {str(round(all_max[var],4)).rjust(20)}, ')
            f.write(f'{round(all_mean[var],4)}, {round(all_median[var],4)}, {round(all_stdev[var],4)}\n')
    summary_stats_df = pd.concat([all_min, all_max, all_mean, all_median, all_stdev], axis=1)
    return summary_stats_df


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




def plot_histograms(data, vars1):   
    for var in vars1:
        plt.figure()
        sns.histplot(data=data, x=var, hue="Class", binwidth=0.2, kde=True)
        plt.savefig(f'plots/histogram_{var}.png')  


#def main():
sns.set_theme()
# Read in the data from the source file - no header  
data = pd.read_csv('data\iris.data', header=None)
# List the column/variable names
variables = ["Sepal Length", "Sepal Width", "Petal Length",\
           "Petal Width", "Class"]

# Assign a header to the data
data.columns = variables

#summary = data.describe()

class_names = data["Class"].unique()
# Slice the dataframe to separate the Iris classes into separate dataframes
# containing only the measurement data
#iseto = data[data["Class"] == "Iris-setosa"].iloc[:, 0:4]
#ivers = data[data["Class"] == "Iris-versicolor"].iloc[:, 0:4]
#ivirg = data[data["Class"] == "Iris-verginica"].iloc[:, 0:4]



# call summary_stats to write a file which summarises the data
# returns a dataframe of the summary stats
data_wo_class = data[variables[:-1]]
#print(data_wo_class.head())
summary_stats_df = summary_stats(data[variables[:-1]], variables[:-1])
summary_stats_df.to_csv("summary/summary of stats.csv")
plot_histograms(data, variables[:-1])

# loop over each iris/class to call summary_stats and histo plots
for item in class_names:
    # Slice data to get just the data related to one class/iris
    iris_data = data[data["Class"] == item]
    vari = variables[:-1]    
#    summary_stats(iris_data, vars, filename=f'summary/{item}_summary.txt')


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
#print("ALL MIN", all_min)
#print("min_PL", min_PL)

#bins = np.arange(math.floor(all_min["Petal Length"]), math.ceil(all_max["Petal Length"])+1, bin_size)
#print(min_data)

#sns.histplot(data=data, x="Petal Length", hue="Class", bins=bins, kde=True)
#plt.savefig("plots/histplot.png")            

    

#if __name__ == "__main__":
#    main()



