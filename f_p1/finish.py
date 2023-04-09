import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = data['whoAmI'].unique()

for category in categories:
    data[category] = 0

for i, row in data.iterrows():
    category = row['whoAmI']
    data.at[i, category] = 1

data = data.drop('whoAmI', axis=1)

data.head()

print(data.head())