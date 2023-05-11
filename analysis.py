'''
HDip in Computing in Data Analytics
PANDS Project 2023
Lecturer: Andrew Beatty
Analysis of Fisher's Iris Dataset
Author: Eilis Donohue (G00006088)
See analysis.ipynb for code, commentary and references
'''
import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.polynomial import Polynomial as P
# Import the datasets module from sklearn to compare the in-built iris dataset
# with the UCI basecase dataset 
from sklearn import datasets

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
def write_to_file(summary_filename, df_data, heading, mode, dec_format="%.2f"):   
    with open (summary_filename, mode) as f:
        # to_string for nice formatting for the text file
        df_summary_asstr = df_data.to_string(float_format=dec_format, 
                                                justify='center')
        # write header and data with new lines in between 
        f.write(f'***************** {heading} *****************\n')
        f.write(f'{df_summary_asstr}\n')
        f.write('\n')

# Function to plot seaborn histograms of data 
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
    # Use the numpy polynomial fit method to get a linear regression (straight
    # line trend)
    linear_fit = P.fit(numpy_x[idx], numpy_y[idx], 1)
    return linear_fit

# Function which calculates a rolling mean and plots this with a linear
# fit and the mean of the set
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
    
def make_subdirs(subdir_list):
    # loop over the subdirs to be created
    for subdir in subdir_list:
        # check if it exists aleady, if so delete contents
        if subdir in os.listdir():
#            Used in development            
#            delete_subfolder_files(subdir)
             pass
        else:
            # if not - create it
            os.makedirs(subdir)

''' Deleting files was used in development. Deleting directory not desirable - 
in case of user already having a directory with files.'''
def delete_subfolder_files(location):
    # delete all files by using wildcard
    location = location + "/*"
    for f in glob.glob(location):
        os.remove(f)

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
# Output the size of the dataframe and then the first 5 lines to get sense of the data
print(f'Dataframe shape is (rows, columns): {data.shape}\n')
print(f'First 5 lines:\n{data.head(5)}\n')      
# Check for any missing values in the dataframe and sum up on rows and columns
print(f'{data.isna().sum().sum()} missing values in dataframe')
# get the different classifications
class_names = data["Class"].unique()
# dataframe without class column
data_wo_class = data.drop(columns="Class").copy()
print("Data read in")

# ***************************** Set up subdirs ******************************
# Set up the subdirectors for the summary stat files and plots
make_subdirs(['summary', 'plots'])

# ********************** Outputting the summary stats ************************    
# Get the statistics for the whole dataset and write to file
df_summary_all = get_summary_stats(data.drop(columns="Class"))
write_to_file(summary_filename, df_summary_all, "All data", "wt")
df_corr_all = get_corr(data)
write_to_file(corr_filename, df_corr_all, "All data", "wt", "%.3f")

# Get summary stats and corr for each class of iris and write to text file
for item in class_names:
    # Extract the data related to one class of iris
    iris_data = data[data["Class"] == item].copy()
    # Strip the class column before passing to function
    iris_data.drop(columns = "Class", inplace=True) 
    # Get the stats and write to file
    df_summary = get_summary_stats(iris_data)
    write_to_file(summary_filename, df_summary, item, "at")
    df_corr =  get_corr(iris_data)
    write_to_file(corr_filename, df_corr, item, "at", "%.2f")   

# Get the pandas dataframe of correlation stats for the whole dataset
df_corr = pd.DataFrame()
df_corr = get_corr(data_wo_class)
print(f"Summary stats in {summary_filename} and {corr_filename}")

# ****************************** Plotting ************************************   
# Generate the pair plot of scatters
sns.set_theme(style='whitegrid')
plt.figure()
g=sns.pairplot(data, hue="Class", diag_kind="kde")
g.map_lower(sns.kdeplot, levels=7, color=".2")
plt.savefig("plots/scatter_pairplot.png")

# Generate the histograms for the 4 iris measurement variables
for var in variables_wo_class:
    plot_histograms(data, var)   
   
# Plot histogram for the full dataset    
plt.figure()
g = sns.histplot(data_wo_class, binwidth=0.2, kde=True)
g.set_xlabel('Measurement (cm)')
plt.savefig('plots/histogram_all_data.png')  

sns.set_theme(style="ticks", )

# # Plot Length v Width for Sepal and Petal with linear regression fit
plt.figure()
sns.lmplot(x ='Petal Width', y ='Petal Length', data = data, hue="Class")
plt.savefig("plots/scatter_petal.png")
plt.figure()
sns.lmplot(x ='Sepal Width', y ='Sepal Length', data = data, hue="Class")
plt.savefig("plots/scatter_sepal.png")


# Create a figure with 4 histogram subplots showing each variable
sns.set_theme(style='white')
fig, ax = plt.subplots(nrows = 2, ncols =2, figsize=(10,8))
sns.histplot(data, x="Petal Length", hue="Class", binwidth=0.2, kde=True, ax=ax[0,0])
sns.histplot(data, x="Petal Width", hue="Class", binwidth=0.2, kde=True, ax=ax[0,1])
sns.histplot(data, x="Sepal Length", hue="Class", binwidth=0.2, kde=True, ax=ax[1,0])
sns.histplot(data, x="Sepal Width", hue="Class", binwidth=0.2, kde=True, ax=ax[1,1])
fig.tight_layout()
plt.savefig("plots/histogram_4plot.png")

print("Plots in /plots")

# ******************************* Further Analysis *****************************
''' For each iris type, create a plot with 4 subplots of the measurements with 
a rolling mean  calculated, a linear fit of that rolling mean and also 
the mean of the dataset''' 
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
     plt.savefig(f'plots/line_RollingMean_{iris}.png')   

# Create variable 'size'     
iris_size = data['Sepal Width'] * data['Sepal Length'] + \
            data['Petal Width'] * data['Petal Length']     
# Create a new dataframe for this makey-uppy variable            
iris_size = pd.DataFrame(iris_size).copy()
iris_size.columns=['Size']
iris_size['Class'] = data['Class']

# Loop over classes in the size dataframe and create a rolling mean plot for
# each iris     
for iris in class_names:
    fig, axs = plt.subplots()   
    data_iris = iris_size[iris_size["Class"] == iris].drop(columns = 'Class').copy()
    data_iris_variable = data_iris.reset_index()
    plot_rollingmean(data_iris_variable, 5, iris, "Size", fig, axs)
    fig.suptitle(iris, fontsize=16)
    axs.legend(['Measured','Rolling Mean', 'Rolling lin_fit', 'Mean'])
    plt.savefig(f'plots/line_RollingMeanSize_{iris}.png')

''' Take all the measurements in the data set and multiply by 10 to get the 
measurement in mm. Then plot a histogram of the first digit of each 
measurement to see if the set satisifies Benford's Law (though Benford's Law 
is more applicable to large numbers)'''

# Multiply the whole dataset of measurements by 10 to get millimetres
data_wo_class_mm = data_wo_class * 10
# Convert the dataset to strings
strdata = data_wo_class_mm.astype(str).copy()
# Stack the columns to get one continuous series of values
stacked = strdata.stack().copy()
# Get the first digit of each value
first_digit = stacked.str[0]
# Convert to a list
first_digit = first_digit.tolist()

# Define a dictionary keylist and empty dict to store the count of each digit
digit_keylist = ['1','2','3','4','5','6','7','8','9']
digit_count_dict = {}
# Loop over the digits to get an ordered dictionary
for key in digit_keylist:
    digit_count_dict[key] = first_digit.count(key)   

# Make a barchart of the dictionary values
plt.figure() 
plt.bar(range(len(digit_count_dict)), digit_count_dict.values(), tick_label=
        list(digit_count_dict.keys()))
plt.xlabel('First Digit')
plt.ylabel('Count')
plt.title('First Digit Count in Iris Dataset')
plt.savefig('plots/barplot_BenfordsLaw.png')
        
# Get the number of times 1 is the first digit as percentage of total
digit1_percent = digit_count_dict['1'] / len(first_digit) * 100
print(f'1 appears as the first digit in {digit1_percent:.0f}% of the measurements')

''' Take the UCI Bezdek iris dataset (also given in the UCI repository) and
compare to the "basecase" data which was analysed above. Also compare basecase to
the sklearn bundled iris dataset'''

# Read in BezdekIris (this is the 2nd dataset included in the UCI repository)
bezdek_iris = pd.read_csv('data/bezdekIris.data', header=None)
bezdek_iris.columns = variables
# Do a comparison between the basecase data and the Bezdek Iris data
print("Comparison between the basecase UCI data and the UCI Bezdek data:")
print(data.compare(bezdek_iris))

# Compare the sklearn dataset with basecase
# Load the sklearn iris dataset - bunch object with different types
sklearn_iris_bunch = datasets.load_iris()
# Get the data 
sklearn_iris = pd.DataFrame(sklearn_iris_bunch.data)
# Data preview - 
#print(sklearn_iris)
#print(sklearn_iris_bunch)
# check if data layout is the same as the UCI datasets - it is
# so can assign the same columns index
print(sklearn_iris_bunch.feature_names) 
print(variables_wo_class)
# Put the dataframe together using the same columns headers to aid comparison
sklearn_iris.columns = variables_wo_class
# Add the class column (which is .target)
sklearn_iris['Class'] = sklearn_iris_bunch.target
# Class is a digit with the reference in .target_names
print(sklearn_iris.head(5))
print(sklearn_iris_bunch.target_names)
# Set up a reference dictionary to replace Class data with the iris name
ref_dict = {}
for i, row in enumerate(sklearn_iris_bunch.target_names.tolist()):
    ref_dict[i] = "Iris-" + row
sklearn_iris['Class']  = sklearn_iris['Class'].replace(ref_dict)
# Compare the sklearn dataset with the basecase
print("Comparison between the basecase UCI data and sklearn dataset:")
print(data.compare(sklearn_iris))



print('Analysis Complete')
