
#%%
#import statements
import pandas as pd
import os
import glob

#%%
#read in data in tsv format

bag=[]

for f in glob.glob("TRJ3/*.tsv"):
    data=pd.read_csv(f,skiprows=13,sep="\t")
    bag.append(data)

#%%
#concatenate all dataframes into one dataframe
df=pd.concat(bag)

#%%
#read in data in excel format

bottle=[]

for a in glob.glob("TRJ3/*.xlsx"):
    usage=pd.read_excel(a,skiprows=13)
    bottle.append(usage)

df1=pd.concat(bottle)


#%%
#read in data in csv format

can=[]

for b in glob.glob("TRJ3/*.csv"):
    stats=pd.read_csv(b,skiprows=13)
    can.append(stats)

df2=pd.concat(can)


#%%
#combining all data into one dataframe or mega spreadsheet

allstats=pd.concat([df,df1,df2])
print(allstats.shape)
print(allstats.head())
allstats.to_csv("counterstats.csv",index=False)
sorteddf=allstats.sort_values("Title")

sorteddf.to_csv("azcounterstats.csv",index=False)


#%% 
#run this for Harrasowitz data
har=pd.read_excel("Harrassowitz.xlsx",sheet_name="Data",skiprows=4)

har=har.dropna(subset=["E-ISSN"])

counter=pd.merge(sorteddf,har,how="inner",left_on="Online_ISSN",right_on='E-ISSN')

essential=counter[['Title', 'Platform',   'Online_ISSN',  'Metric_Type', 'Reporting_Period_Total',  'Product title','E-ISSN', 'Total price']]
essential=essential[essential.Metric_Type=='Unique_Item_Requests']
essential.to_csv("analyzedusage.csv",index=False)
# %%
