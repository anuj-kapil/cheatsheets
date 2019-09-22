from numpy import array
# Vector
v1 = array([2, 3, 5, 7])
v2 = array([3, 5, 1, 4])
print(v1)
print(v2)
print(v1+v2)
type(v1)

# Matrix

m1 = array([2, 3, 5, 7])
m1 = m1.reshape(2,2)

m2 = array([[3, 5],[1, 4]])

print(m1+m2)
help(array)
# Order needs to be changed

#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# list
id = [2,3,5,7]
name = ['Jon','Jane','John','Jean']
lst = [id,name]
lst[0][1]

# Dict
dct = {
        'id':id,
        'name':name
    }
dct

import pandas as pd

# Data Frame
df = pd.DataFrame(dct)

import os
output_dir = os.getcwd() + '/Data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
else:
    print("Dir already exists!")


df.to_csv('Data/employees.csv', index=False)

dt_r = pd.read_csv('Data/employees.csv')


# Bind new columns
age = {'age':[30, 25, 35, 29]}
height = {'height':[1.7, 1.8, 1.65, 1.85]}
dt_r = pd.concat([dt_r, pd.DataFrame(age)], axis=1)
dt_r = pd.concat([dt_r, pd.DataFrame(height)], axis=1)

# Bind new rows
# new row is defined as a dict first (each item as a list) and then as pandas dataframe
new_row = {
        'id':[9],
        'name':['Jen'],
        'age':[31],
        'height':[1.6]
    }
dt_r = pd.concat([dt_r, pd.DataFrame(new_row)])


# Data Wrangling

## Descriptive statistics
dt_r.describe(include = 'all')

## Removing NULLS
dt_r[~dt_r['name'].isnull()]
dt_r.isnull().values.any()


area = 8.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")