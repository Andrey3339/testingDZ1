# Задание 44  В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(lst, columns = ['whoAmI'])
data.head()

lst = []
for el in data.whoAmI:
    if el == 'robot':
      lst.append([1, 0])
    else:
      lst.append([0, 1])

df = pd.DataFrame(lst, columns = ['robot', 'human'])
df.head()


