# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'}, inplace='True') 
data.head(10)





# --------------
#Code starts here




#data["Better_Event"] = np.where(data['Total_Summer'] >data['Total_Winter'] , 'Summer','Winter')

data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', np.where(data['Total_Summer']<data['Total_Winter'], 'Winter', 'Both'))

better_event = data["Better_Event"].value_counts().index[0]


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries=top_countries.iloc[:(len(top_countries)-1)]

def top_ten(data,column):
    top_10_summer = np.array([])
    result = data.nlargest(10,column)
    country_list = result['Country_Name'].tolist()
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

set1 = set(top_10_summer).intersection(set(top_10_winter))
common = list(set1.intersection(set(top_10)))
common





# --------------
#Code starts here

summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]


# --------------
#Code starts here



summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']

temp = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]

summer_max_ratio = temp['Golden_Ratio']

summer_country_gold = temp['Country_Name']

# For Winter df
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

tempWinter = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]

winter_max_ratio = tempWinter['Golden_Ratio']

winter_country_gold = tempWinter['Country_Name']

# Top df
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

temptop = top_df.loc[top_df['Golden_Ratio'].idxmax()]

top_max_ratio = temptop['Golden_Ratio']

top_country_gold = temptop['Country_Name']





# --------------
# Code starts here


data_1 = data.drop(data.tail(1).index)

data_1['Total_Points'] = data_1.Gold_Total * 3 + data_1.Silver_Total * 2 + data_1.Bronze_Total

most_points = data_1.Total_Points.max()
country_id = data_1.Total_Points.idxmax()
best_country = data_1.loc[country_id][0]

print(best_country)
print(most_points)


# --------------
#Code starts here


best = data[data["Country_Name"]==best_country]
best.reset_index(drop=True,inplace=True)
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

#PLotting bar plot
best.plot.bar(stacked=True)

#changing x-axis label
plt.xlabel("United States")

#changing x=y-axis label
plt.ylabel("Medals Tally")

#Rotating nthe Ticks of X-axis
plt.xticks(rotation=45)





