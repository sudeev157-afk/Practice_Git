#Grouping and Aggregation

#Load the dataset
import pandas as pd
df = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/Flavors (1).csv')
print(df)

#grouping by group by and using aggregation for printouts
group_by_flavor = df.groupby('Base Flavor')
print(group_by_flavor.mean(numeric_only=True))
