#Indexing

import pandas as pd
df = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/world_population.csv')
print(df)

#Setting country as idex coloum
df = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/world_population.csv', index_col = 'Country')
print(df)

#Reversing the index
df.reset_index(inplace=True)
print(df)

#Creating a new index also saving it
print(df.set_index('Country', inplace=True))

#Using loc to look over location of string data
print(df.loc['Albania'])

#Using loc to look over data through integer location
print(df.iloc[1])

#Reversing the index
df.reset_index(inplace=True)
print(df)

#Creating multiple indexes on continent & country
df.set_index(['Continent', 'Country'], inplace = True)
print(df)

#Sorting the indexes
print(df.sort_index())
pd.set_option('display.max.rows', 235)
print(df)

#Sorting the index in descending order
df.sort_index(ascending=False)
pd.set_option('display.max.rows', 235)
print(df)

#Sorting the index, first in descending order, second in ascending
df.sort_index(ascending=[False, True])
pd.set_option('display.max.rows', 235)
print(df)

#Looks for data in first index and then second index
print(df.loc['Africa','Angola'])

#Integer loc goes in individual indexing not on multi indexing
print(df.iloc(1))