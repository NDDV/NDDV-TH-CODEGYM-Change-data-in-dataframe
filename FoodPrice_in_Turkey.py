#%%
import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
df

# %%
df.rename(columns={'Place':'Địa điểm','ProductName':'Tên SP'},inplace=True)
df['new_column'] = 'NaN'
df['Giảm giá']= pd.Series('10%', index=df.index) #index là gán 10% cho hết tất cả các dòng
df.head()
# %%
df.insert(10,'Giảm giá 2',pd.Series('12%', index=df.index))
df.head()

# %%
df=df.append({'Địa điểm':'NA','ProductId':'RR','Tên SP':'Rice',
                'UmId':10,'UmName':'KG','Month':6,'Year':2021,
                'Price':84.3785,'Giảm giá':'10%','Giảm giá 2':'12%'},
                ignore_index=True)
df.tail()

# %%
del df['new_column']
df.pop('Giảm giá 2')
df.drop('Giảm giá', axis=1, inplace=True)
df.head()
#%%
df.drop(1, axis = 0, inplace=True)
df.head()

# %%
df.drop([7377,7379], inplace=True)
df

# %%
