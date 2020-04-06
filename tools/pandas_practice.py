#
# Author: Ronnie Ankner 2/1/2019
# Purpose: To learn and become more familiar with the Pandas Data Processing package

import pandas as pd
import numpy

#Pandas easily interfaces with Matplotlib and is built on top of Numpy so many of the numpy functions still work
# Core components:
#	- Series: one column of data
#	- Dataframe: multidimensional dataset

#================== INITIALIZING DATA FRAMES ===============================
#******Dictionary method*******:
data = {'cucumba': [1,2,4,5,5,3,34,23,24,3],'kiwi': [1,2,4,5,5,3,34,23,24,3]}

fruits = pd.DataFrame(data)
print("Standard Initialization: (", type(fruits), ")")
print(fruits)

#creates a 10x2 grid with fruits as the columns and the numbers populating the rows
#to initialize with a specific index:
tab_index = ['a','b','c','d','e','f','g','h','i','j']

fruits = pd.DataFrame(data, index=tab_index)
print("With Index Changed: (", type(fruits), ")")
print(fruits)

#locating data:
single_row = fruits.loc['b']
print("Single Row: (", type(single_row), ")")
print(type(single_row))


#*****Reading From CSV*******
new_data = pd.read_csv("sample_file.csv", index_col=0)
#index_col set to 0 since csv's dont have indexes

#*****Reading From JSON*******
new_data = pd.read_json('sample_file.json')

#You Can do SQL database connection, but we'll get to that later

#================== Storing into a Data type =============================

#df.to_csv('new_purchases.csv')

#df.to_json('new_purchases.json')

#df.to_sql('new_purchases', con)

#================== Data Operations ===================================
#******* Viewing Data *******
fruits.head() #-> first 5 rows
fruits.head(10) #-> first 10 rows
fruits.tail() #-> last 5 rows

#************** Getting information about the data *************
fruits.info() #-> general info about type and size
fruits.shape #-> attribute that provides tuple (rows, columns)

#*********** Adding to the set ***************
fruits.append(data)

#********* Removing Duplicates ***************
fruits.drop_duplicates()
#assigning "inplace=True" to any operation will force it to occur on the variable without needing to reassign 
fruits.drop_duplicates(inplace=True)
#changing the "keep" argument indicates which of the duplicate rows are kept, either first, last, or False (drop all duplicates)
fruits.drop_duplicates(inplace=True, keep=False)   

#******** Column Operations **************
fruits.columns #-> outputs column indexes(names)
#can change column names very easily with dict objects
fruits.rename(columns={'cucumba': 'cucumber', 'kiwi': 'KIWI'}, inplace=True)
#can change columns explicitly
fruits.columns=['cucumber', 'KIWI']
#making lower case for example:
fruits.columns=[col.lower() for col in fruits]

#********* NULL Values ****************
#Can be python type "None" or Numpy type "np.nan"
fruits.isnull() #-> returns a DataFrame where False indicates NOT NULL and True indicates NULL
#to get number in each column:
fruits.isnull().sum()
#removing nulls:
fruits.dropna() #-> removes any row with 1 or more nulls
#removing nulls by column: set axis = 1
# -> axis points to shape tuple (rows, columns) where rows=0 and columns=1
fruits.dropna(axis=1) #-> removes any column with 1 or more nulls

#************** Data Operations *******************
#Selecting a specific column
cuc = fruits['cucumber']
#Getting Mean of the column
cuc.mean()
#Getting Pretty much all basic statistical information
fruits.describe()
#Count Occurances of certain values and output
fruits.value_counts().head(10)
#get correlation between variables
fruits.corr()
#accessing by row (ONLY A DATAFRAME ATTRIBUTE)
#locate by name
var = fruits.loc["example"]
#locate by index
var = fruits.iloc[1] #single value 
var = fruits.iloc[1:4] #for a range [a, b)****















