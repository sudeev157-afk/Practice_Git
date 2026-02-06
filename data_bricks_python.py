# Loading pandas library and giving aliasing
import pandas as pd

#Loading and reading data file as csv
df = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/countries of the world.csv')
print(df)

#Reading csv file as a table removing delimeters
df_txt = pd.read_table(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/countries of the world.csv', sep = ',')
print(df_txt)

# Reading csv file as csv removing delimiters
df_csv = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/countries of the world.csv', sep = '\t')
print(df_csv)

# Reading the json file in python
df_json = pd.read_json(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/json_sample.json')
print(df_json)

#Read the excel files
df_excel = pd.read_excel(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/world_population_excel_workbook.xlsx')
print(df_excel)

#Read the excel files and select certain sheet
df_excel2 = pd.read_excel(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/world_population_excel_workbook.xlsx', sheet_name = 'Sheet1')
print(df_excel2)

#Show all the data files or all elements for rows
pd.set_option('display.max.rows', 235)
print(df_excel)

#Show all the columns of jsonfile for column
pd.set_option('display.max.column', 50)
print(df_json)

#Get the information of the data file excel we been wprking on
df_excel.info()

#Get more data info which is shape of data
print(df_excel.shape)

#View certain required first values of data file
print(df_excel.head(5))

#View the demanded values from last
print(df_excel.tail(10))

#Only see only one colum data in file
print(df_excel['Rank'])

#Look onlly certain or individual data point select by index label or column names
print(df_excel.loc[225])

#Integer position indexing
print(df_excel.iloc[225])

#Look onlly certain or individual data point select by index label or column names ignore capitalization and spaces
df_excel['Country'] = df_excel['Country'].str.strip()        # remove spaces
df_excel['Country'] = df_excel['Country'].str.title()        # normalize capitalization

print(df_excel[df_excel['Country'] == 'Uzbekistan'])

