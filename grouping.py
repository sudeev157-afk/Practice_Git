#Grouping and Aggregation

#Load the dataset
import pandas as pd
df = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/Flavors (1).csv')
print(df)

#grouping by group by and using aggregation for printouts
group_by_flavor = df.groupby('Base Flavor')
print(group_by_flavor.mean(numeric_only=True))

#Grouping based on count of aggregation
group_by_flavor = df.groupby('Base Flavor')
print(group_by_flavor.count())

#Grouping based on minimum of aggregation
group_by_flavor = df.groupby('Base Flavor')
print(group_by_flavor.min())

#Grouping based on maximum of aggregation
group_by_flavor = df.groupby('Base Flavor')
print(group_by_flavor.max())

#Grouping based on sum of aggregation
group_by_flavor = df.groupby('Base Flavor')
print(group_by_flavor.sum())

#Performing aggregation using multiple functions
agg_by_rating = df.groupby('Base Flavor').agg({'Flavor Rating': ['mean', 'max', 'count', 'sum'], 'Texture Rating': ['mean', 'max', 'count', 'sum']})
print(agg_by_rating)

#Grouping based on multiple columns
group_by_column = df.groupby(['Base Flavor', 'Liked']).mean(numeric_only=True)
print(group_by_column)

#HIgh level overview of aggregations
group_by_describe = df.groupby('Base Flavor').describe()
print(group_by_describe)