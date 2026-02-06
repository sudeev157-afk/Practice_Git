#Filtering and Ordering

#Load the dataset
import pandas as pd
df = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/world_population.csv')
print(df)

#Filtering the column - Rank less than 10
print(df[df['Rank']<=10])

#Loking for specific data within the column or called as specific observations#
specific_countries = ["Bangladesh", "Brazil"]
print(df[df['Country'].isin(specific_countries)])

#Using contains string function to look for single observation
print(df[df['Country'].str.contains('United')])

#Setting the data index
df2 = df.set_index('Country')
print(df2)

#Using the filter function
print(df2.filter(items = ['Continent', 'CCA3']))

#Using axis
print(df2.filter(items = ['Continent', 'CCA3'], axis = 1))

#Using axis to filter certain country on 0 axis
print(df2.filter(items = ['Zimbabwe'], axis = 0))

#Using like function
print(df2.filter(like = 'United', axis = 0))

#Using loc function- string location function
print(df2.loc['United States'])

#Using iloc function - integer location function
print(df2.iloc[3])  #Looks for 3rd position

#Sorting and ordering
print(df)

#Sorting data based on rank column and ordering in ascending order
print(df[df['Rank'] <10].sort_values(by='Rank', ascending = True))

#Sorting data based on rank column and ordering in descending order
print(df[df['Rank'] <10].sort_values(by='Rank', ascending = False))

#Sorting in group 
print(df[df['Rank'] <10].sort_values(by=['Country','Rank'], ascending = False))

#Sorting multiples but first country-descending and rank in ascending
print(df[df['Rank'] <10].sort_values(by=['Country','Rank'], ascending = [False, True]))
