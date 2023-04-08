import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем уникальный список категорий
categories = data['whoAmI'].unique()

# Создаем пустые столбцы для каждой уникальной категории
for category in categories:
    data[category] = 0

# Заполняем бинарными значениями столбцы, соответствующие категориям
for i, row in data.iterrows():
    category = row['whoAmI']
    data.at[i, category] = 1

# Удаляем исходный столбец 'whoAmI'
data = data.drop('whoAmI', axis=1)

data.head()

print(data.head())
