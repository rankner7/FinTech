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





