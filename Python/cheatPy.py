#%%
import numpy as np
import pandas as pd
import os
import re

#%%
# Vector
v1 = np.array([2, 3, 5, 7])
v2 = np.array([3, 5, 1, 4])
print(v1)
print(v2)
print(v1+v2)
type(v1)

# Matrix

m1 = np.array([2, 3, 5, 7])
m1 = m1.reshape(2,2)
m1 = m1.T
m2 = np.array([[3, 5],[1, 4]])
m2 = m2.T
print(m1+m2)

# Order needs to be changed

#There are four collection data types in the Python programming language:

#%%
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

# Data Frame
df = pd.DataFrame(dct)

df
dt_r = df
#%%

output_dir = os.getcwd() + '/Data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
else:
    print("Dir already exists!")



df.to_csv('Data/employees.csv', index=False)
df
dt_r = pd.read_csv('Data/employees.csv')

#%%
# Bind new columns
age = [30, 25, 35, 29]
dt_r['age']=age

height = [1.7, 1.8, 1.65, 1.85]
dt_r['height']=height

# Another way
# age = {'age':[30, 25, 35, 29]}
# height = {'height':[1.7, 1.8, 1.65, 1.85]}
# dt_r = pd.concat([dt_r, pd.DataFrame(age)], axis=1)
# dt_r = pd.concat([dt_r, pd.DataFrame(height)], axis=1)

# Bind new rows
# new row is defined as a dict first (each item as a list) and then as pandas dataframe
new_row = {
        'id':[9],
        'name':['Jen'],
        'age':[31],
        'height':[1.6]
    }
dt_r = pd.concat([dt_r, pd.DataFrame(new_row)], ignore_index=True)

# Ignore index
#%%
# Data Wrangling

## Descriptive statistics
dt_r.describe(include = 'all')

#%%
## Removing NULLS
dt_r[~dt_r['name'].isnull()]
dt_r.isnull().values.any()

#%%
## Removing Duplicates
# Add a duplicate
dt_r = pd.concat([dt_r, pd.DataFrame(new_row)], ignore_index=True)

dt_r = dt_r.drop_duplicates()

#%%
## Select rows/columns
### Rows
dt_r.iloc[0:2]
dt_r[dt_r['name']=='Jon']

### Columns
dt_r.iloc[:,0:2]
dt_r[['name','id']]

### Rows & Columns
dt_r.loc[dt_r['name']=='Jon', ['name','id']]

#%%
## Where clause
## group by
## order by

weight = [75,60,70,65,50]
dt_r['weight'] = weight

gender = ['M','F','M','F','F']
dt_r['gender'] = gender

# weight = {'weight':[75,60,70,65,50]}
# gender = {'gender':['M','F','M','F','F']}
# dt_r = dt_r.reset_index(drop=True)

# dt_r = pd.concat([dt_r, pd.DataFrame(weight)], axis=1)
# dt_r = pd.concat([dt_r, pd.DataFrame(gender)], axis=1)

dt_r.loc[dt_r['weight']>60,'gender'].value_counts()
# Default sorts on frequencies and order in descending
#%%
# Data Transformation

# Convert height in metres to inches and save as another column

dt_r['height_inch'] = dt_r['height']*39.37

#%%
# Drop columns

del dt_r['height_inch']
# or
dt_r = dt_r.drop(columns=['height_inch'])

dt_r['height_inch'] = dt_r['height']*39.37
dt_r['height_inch'] = dt_r.height*39.37

#%%
# Long form
dt_r_l = pd.melt(dt_r, id_vars=['name'], value_vars=['id','age','height','weight'])

#%%
# Wide form
#pd.crosstab(index=dt_r_l['name'], columns=dt_r_l['variable'], values=dt_r_l['value'], aggfunc='first').reset_index()
dt_r_w = dt_r_l.pivot_table(values='value', index='name', columns='variable').reset_index()

#%%
#Data Join and Rolling Join

address_dt = pd.DataFrame()

address_id = [1,2,3,4,5]
address_array = ['1640 Riverside Drive, Hill Valley, California'
                   ,'344 Clinton St., Apt. 3B, Metropolis, USA'
                   ,'12 Grimmauld Place, London, UK'
                   ,'221B Baker Street, London, UK'
                   ,'1313 Webfoot Walk, Duckburg, Calisota']

address_dt['address_id'] = address_id
address_dt['address'] = address_array

address_id = [1,2,3,5,5]
dt_r['address_id'] = address_id

#%%
# RIGHT JOIN
dt_r.merge(address_dt, how='right')

#%%
# INNNER JOIN
dt_r.merge(address_dt)

#%%
# LEFT JOIN
dt_r.merge(address_dt, how='left')

#%%
dt_r[dt_r['name'].str.contains("o")]
dt_r['name'].str.contains("o")

dt_r['name'],dt_r['name'].str[:1],dt_r['name'].str[-2:-1]



dt_r['name']

#Regex

dt_r.loc[dt_r['name'].str.contains('^J'),['name']]
dt_r.loc[dt_r['name'].str.contains('n$'),['name']]

#%%
# Date and Time

birth_date = ['1989-03-01','1994-09-09','1984-07-15','1990-05-01','1988-06-03']
# String Object
dt_r['birth_date'] = birth_date
dt_r.birth_date.dtype

dt_r.birth_date.dtypes
# Date Object
dt_r['birth_date'] = pd.to_datetime(dt_r['birth_date'])

# Days since epoch
#%%
dt_r['birth_date'] = pd.to_datetime(dt_r['birth_date'])- pd.datetime(1970,1,1)

#%%
plt = dt_r.plot.scatter(x='height',y='weight')
#%%

#%%
import seaborn as sns
sns.pairplot(x_vars=["height"], y_vars=["weight"], data=dt_r, hue="gender", size=5)
#%%

area = 8.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")


dt_r.head(2)       # first five rows
dt_r.tail(2)       # last five rows
dt_r.sample(2)    # random sample of rows
dt_r.shape        # number of rows/columns in a tuple
dt_r.describe()   # calculates measures of central tendency
dt_r.info()       # memory footprint and datatypes

#%%

type(dt_r.age)

dt_r.birth_date.dtype