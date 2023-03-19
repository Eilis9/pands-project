'''
PANDS Project 2023
Fischer's Iris Dataset
Author: Eilis Donohue
'''

import pandas as pd
  
data = pd.read_csv('data\iris.data')
#columns = pd.read_csv('data\iris.names')
#print(columns)
columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]

data.columns = columns
sepal_width_mean = data["Sepal Width"].mean()

#data.mean()
#print(data)