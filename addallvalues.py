#%%
import pandas as pd
#%%
#read in counterstats.csv
df = pd.read_csv('counterstats.csv')
#%%
df.head()
# %%
# new dataframe with rows containing Unique_Item_Requests
df2 = df[df['Metric_Type'] == 'Unique_Item_Requests']
# %%
df2.head()
# %%
# sum column Reporting_Period_Total
df2['Reporting_Period_Total'].sum()
# %%
