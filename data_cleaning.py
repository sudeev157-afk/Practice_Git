#Install required libraries
import pandas as pd
import numpy as np
df = pd.read_excel('/Users/sudipbhandari/Desktop/Python_learning/git-practice/Customer Call List.xlsx')
#print(df)

#Drop the duplicates
df = df.drop_duplicates()
#print(df)

#Droping or deleting specefic column
df= df.drop(columns =['Not_Useful_Column'])
print(df)

#Clean the column refrences data
df['Last_Name'] = df['Last_Name'].str.strip('/._')
#print(df)

#Individual ways 
#df['Last_Name'] = df['Last_Name'].str.lstrip(/)
#df['Last_Name'] = df['Last_Name'].str.lstrip(...)
#df['Last_Name'] = df['Last_Name'].str.rstrip(_)
#print(df)

#Replace the individual character from dataset
df['Phone_Number'] = df['Phone_Number'].str.replace('/', '', regex = True)
print(df)

#Clean the number column
df['Phone_Number'] = df['Phone_Number'].str.replace(r'\D', '', regex = True)
pd.set_option('display.max.columns', None)
#print(df)

#Applying lamda technique first convertin data type to strings due to data understanding issues
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
print(df)

#Working with nan or null values in phone number column
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')
df['Phone_Number'] = df['Phone_Number'].str.replace('--', '')
df['Phone_Number'] = df['Phone_Number'].str.replace('na', '')
print(df)

#Splitting the address coolumn into three seperates column 
df[['Street_Address', 'State', 'Zip_Code']] = df['Address'].str.split(',',n=2, expand = True)
print(df)

#Cleaning paying customers column
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y', regex=False)
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N', regex=False)
print(df)

#Cleaning do_bot_contact column
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y', regex=False)
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N', regex=False)
print(df)

#Checkingg the data types
print(df.dtypes)

#Working with nulls and nan values
df = df.replace("N/a", '')
#df = df.replace("NaN", '')
print(df)

#Fill the nan as occupied as not a number value with the blank
df = df.fillna('')
print(df)

#Remooving the yes for do not contact column
#df = df[df['Do_Not_Contact'] != 'Y']
df.drop(df[df['Do_Not_Contact'] == 'Y'].index, inplace=True)
print(df)

#Giving the balnk spaces the N in Do not contact so they aligns with our understanding
#df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('', 'N')
#print(df)

#Remooving the blanks for phone number column
#df = df[df['Phone_Number'] != '']
df.drop(df[df['Phone_Number'] == ''].index, inplace=True)
#df = df.dropna(subset = 'Phone_Number', inplace = True)
print(df)

#Reset the index for normalizations
df = df.reset_index(drop = True)
print(df)

#Saving the final cleaned data file
#df.to_csv('cleaned_data.csv', index=False)
