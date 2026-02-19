#Install required libraries
import pandas as pd
df = pd.read_excel('/Users/sudipbhandari/Desktop/Python_learning/git-practice/Customer Call List.xlsx')
#print(df)

#Drop the duplicates
df = df.drop_duplicates()
#print(df)

#Droping or deleting specefic column
#df= df.drop(columns =['Not_Useful_Column'])
print(df)

#Changes on data in column
df['Last_Name'] = df['Last_Name'].str.strip('/._')
print(df)