#Load the datafile
import pandas as pd
df1=pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/LOTR.csv')
#print(df1)
df2 = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/LOTR 2.csv')
#print(df2)

#Merges
print(df1.merge(df2)) #default inner join

#Inner joint - column name collision during a merge/join
merged_df = df1.merge(df2, how = 'inner', on = 'FellowshipID')
print(merged_df)

#Inner joint - solved column name collision during a merge/join
merged_df2 = df1.merge(df2, how ='inner', on = ['FellowshipID', 'FirstName'])
print(merged_df2)

#Outer joins
merged_df3 = df1.merge(df2, how = 'outer')
print(merged_df3)

#Left join
merged_df4 = df1.merge(df2, how = 'left')
print(merged_df4)

#Right join
merged_df5 = df1.merge(df2, how = 'right')
print(merged_df5)

merged_df6 =pd.merge(df1, df2, on = 'FellowshipID', how ='right')
print(merged_df6)

#Cross joins so comparing each of data values form left with each of right column cross matches left is priority compares with right
merged_df7 = df1.merge(df2, how = 'cross')
print(merged_df7)

#Using joins functions
join_df1 = df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_left', rsuffix = '_right')
print(join_df1)

#Setting index and then joining
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_left', rsuffix = '_right')
print(df4)

#Setting index and then joining outer join 
df5 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_left', rsuffix = '_right', how = 'outer')
print(df5)


#Concatinate - puting one dataframe on top of the other
concat_df1 = pd.concat([df1,df2])
print(concat_df1)

#Concat and inner join
concat_df2 = pd.concat([df1,df2], join = 'inner')
print(concat_df2)

#Concat and outer join
concat_df3 = pd.concat([df1,df2], join = 'outer')
print(concat_df3)

#Concat and outer join on axis
concat_df3 = pd.concat([df1,df2], join = 'outer', axis =1)
print(concat_df3)

#Append the dataframe not in extinsion anymore in this version
#append_df1 = df1.append(df2)
#print(append_df1)