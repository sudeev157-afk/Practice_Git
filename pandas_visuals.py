#Installing required python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv(r'/Users/sudipbhandari/Desktop/Python_learning/git-practice/Ice Cream Ratings.csv')
df = df1.set_index('Date')
print(df)

#Basic regular plot default as line graph
df.plot()
plt.show()

#Line graph ploting
df.plot(kind = 'line')
plt.show()

#Line graph ploting using subplots for multiple plots
df.plot(kind = 'line', subplots= True)
plt.show()

#Advance Line graph ploting
#df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')
plt.show()

#Bargraph plotting
df['Flavor Rating'].plot(kind = 'bar', stacked= True)
plt.show()

#Horizontal bar graph - barh: means horizontal
df.plot.barh(stacked= True)
plt.show()

#Scatterplot
df.plot(kind= 'scatter', x = 'Texture Rating', y = 'Overall Rating',  title = 'Scatterplot', xlabel = 'X-coordinates Texture.R', ylabel = 'Y-coordinates Overall.R')
plt.show()

#Scatterplot more edits
df.plot(kind= 'scatter', x = 'Texture Rating', y = 'Overall Rating', s = 100, c = 'yellow')
plt.show()

#Histogram
df.plot.hist(bin = 20)
plt.show()

#Box[lot]
df.plot.box()
df.boxplot()
plt.show()

#Areaplot
df.plot.area(figsize = (10,5))
plt.show() 


#Check the default color theme available and pick one 
print(plt.style.available)
plt.style.use('tableau-colorblind10')


#Piecharts
df.plot.pie(y ='Flavor Rating', figsize = (10,5))
plt.show()
