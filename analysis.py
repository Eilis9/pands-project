'''
PANDS Project 2023
Fischer's Iris Dataset
Author: Eilis Donohue (G00006088)
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
import os

summary_filename = "Summary_Statistics.txt"

# Function to calculate the basic statistics of the dataset
def get_summary_stats(data, item=''):
    # Get some basic stats 
    summary_df = pd.DataFrame()
    summary_df['Min (cm)'] = data.min()
    summary_df['Max (cm)'] = data.max()
    summary_df['Mean (cm)'] = data.mean()
    summary_df['Median (cm)'] = data.median()
    summary_df['StDev (cm)'] = data.std()
    
    return summary_df

def print_summary_stats(summary_filename, df_data, heading):
    
    with open (summary_filename, 'at') as f:
        df_summary_asstr = df_data.to_string(float_format='%.2f', 
                                                justify='center')
        # to format the header nicely
        filler = "*" * 2
        f.write(f'{filler} {heading} {filler} \n')
        f.write(f'{df_summary_asstr}\n')
        f.write('\n')

def plot_histograms(data, vars1):   
    for var in vars1:
        plt.figure()
        sns.histplot(data=data, x=var, hue="Class", binwidth=0.2, kde=True)
        plt.savefig(f'plots/histogram_{var}.png')  



# Read in the data from the source file - no header  
data = pd.read_csv('data/iris.data', header=None)
# Make a list of the columns
variables = ["Sepal Length", "Sepal Width", "Petal Length",
             "Petal Width", "Class"]

# Assign the header to the data
data.columns = variables

# get the different classifications

class_names = data["Class"].unique()
data_wo_class = data[variables[:-1]]

os.remove(f'summary/{summary_filename}')
# get the statistics for the whole dataset
df_summary_all = get_summary_stats(data.drop(columns="Class"))
# print to file
print_summary_stats(f'summary/{summary_filename}', df_summary_all, "All data")

# Get summary statistics for each class of iris and print to csv
for item in class_names:
    # Extract the data related to one class of iris
    iris_data = data[data["Class"] == item].copy()
    # Strip the class column before passing to function
    iris_data.drop(columns = "Class", inplace=True) 
    df_summary = get_summary_stats(iris_data)    
    print_summary_stats(f'summary/{summary_filename}', df_summary, item)
    

        
        
plot_histograms(data, variables[:-1])
        


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

    #def main():
sns.set_theme()

#if __name__ == "__main__":
#    main()



