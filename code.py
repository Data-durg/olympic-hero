# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
#.rename(columns={'Total_Medals':'Total'}, inplace=True)
data.head(10)
#Code starts here



# --------------
#Code starts here
import numpy as np
data['Better_Event']=np.where(data.Total_Summer>data.Total_Winter,'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 

better_event=data.Better_Event.value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(146,inplace=True)
country_list=[]
def top_ten(top,column):
    country_list=top.nlargest(10,column)
    return country_list
top_10_summer=list(top_ten(top_countries,'Total_Summer').iloc[:,0])
top_10_winter=list(top_ten(top_countries,'Total_Winter').iloc[:,0])
top_10=list(top_ten(top_countries,'Total_Medals').iloc[:,0])
new_total=set(top_10_summer).intersection(set(top_10_winter))
common=list(set(top_10).intersection(new_total))


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
summer_df[['Country_Name','Total_Medals']].set_index('Country_Name').plot(kind='bar')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)
winter_df[['Country_Name','Total_Medals']].set_index('Country_Name').plot(kind='bar')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)
top_df[['Country_Name','Total_Medals']].set_index('Country_Name').plot(kind='bar')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df.set_index('Country_Name')['Golden_Ratio'].idxmax()
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df.set_index('Country_Name')['Golden_Ratio'].idxmax()
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df.set_index('Country_Name')['Golden_Ratio'].idxmax()


# --------------
#Code starts here



data_1=data.drop(146)
data_1['Total_Points']=(data_1['Gold_Total'])*3 + (data_1['Silver_Total'])*2 + (data_1['Bronze_Total'])*1
most_points=data_1['Total_Points'].max()
best_country=data_1.set_index('Country_Name')['Total_Points'].idxmax()


# --------------
#Code starts here
best=data[data['Country_Name']==best_country][['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


