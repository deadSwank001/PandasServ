

# -*- coding: utf-8 -*-
#"""
#Spyder Editor
#DB project 1
#4/25/23 script file.
#"""

import pandas as pd
import numpy as np
import sklearn as sklearn
import matplotlib

#imputer start
#Imputation Technique
from sklearn.impute import SimpleImputer

data = pd.read_csv('C:\\Users\\swank\\OneDrive\\Desktop\\311_Service_Requests_from_2010_to_Present.csv', dtype="object")

#dtype=data
#low_memory=False


print(data.head())

#Head^ size and shape
shape = data.shape
print("Shape {}".format(shape))

size = data.size
print("Size = {}".format(size))


##
print(data.info())




#data.plot.bar(x = 'Name', y = ['Address Type','Location'], rot = 40)
data.plot.bar(x = 'Complaint Type', y = [0, 1], rot = 40)
#print(bar)



#At this point I've covered the first task:
    #Understand the dataset: 1.1 Import the data
    
    #1.2 Visualize the data set[Will be covered more]
    #1.3 Print the columns of the DataFrame
    #1.4 Identify the shape of the dataset(this is done)
    #1.5 Identify the varibles with null values

###"""
#"""fig, ax1=plt.subplots(2, 1), plt.figure()# creating subplot for x variable on left side and plotting it as bars using `matplotlib` library
#ax1 = fig.add_axis([0.,5],'x') # adding axis to the figure with limits of [0,5] in y-direction (y)
#fig=plt.figure()# creating subplot for x variable on left side and plotting it as bars using `matplotlib` library
#ax1 = fig.add_axis([0.,5],'x') # adding axis to the figure with limits of [0,5] in y-direction (y)
#fig=plt.figure()# creating subplot for x variable on left side and plotting it as bars using `matplotlib` library"""
###

#imp_values = SimpleImputer(missing_values = np.nan, strategy = 'mean')

#PHP -> XML -> JSON -> RevShell -> Powershell Empire -> SPPD back orifice backtrace
#cleaner input data [accidental ping]
#Mandarin Chinese -> WingDings -> Regex ... FlipperZero -> Tim Hansen -> 3 months in psyche ward for harboring illegal beliefs
#python 3.10.9 main, Mar 1 2023, packaged by Anaconda, Inc.
#MSC v.1916 64 bit (AMD64)
#"copyright", "credit", "license", "more information"
#IPython 8.10.0