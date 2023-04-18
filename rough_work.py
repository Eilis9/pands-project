# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:53:48 2023

@author: Eilis.Donohue
"""

def write_summary(summary_data, filename='summary/variable_summary.txt'):

    # Write some summary files for the basic stats
    with open (filename, 'wt') as f:
        # Write file header
        f.write(f'Variable, Min (cm), Max (cm), Mean (cm), Median(cm), Standard Deviation (cm)\n')
        # for each variable write a new line
        for var in vari:           
            f.write(f'{str(var).ljust(20)}){str(round(all_min[var], 4)).rjust(20)}, {str(round(all_max[var],4)).rjust(20)}, ')
            f.write(f'{round(all_mean[var],4)}, {round(all_median[var],4)}, {round(all_stdev[var],4)}\n')
            summary_stats_df = pd.concat([all_min, all_max, all_mean, all_median, all_stdev], axis=1)
            
            
 def describe_df(df, class_item):
   return data[data["Class"] == class_item].describe()



# Slice the dataframe to separate the Iris classes into separate dataframes
# containing only the measurement data
#iseto = data[data["Class"] == "Iris-setosa"].iloc[:, 0:4]
#ivers = data[data["Class"] == "Iris-versicolor"].iloc[:, 0:4]
#ivirg = data[data["Class"] == "Iris-verginica"].iloc[:, 0:4]


plt.grid(which='major', linestyle='-', linewidth=0.6)
plt.grid(which='minor', linestyle='-.', linewidth=0.4)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))

#fig, ax = plt.subplots()