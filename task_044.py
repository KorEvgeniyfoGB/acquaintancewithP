import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data['human'] = [1 if i == 'human' else 0 for i in lst]
data['robot'] = [1 if i == 'robot' else 0 for i in lst]
#del data['whoAmI'] #закоментил что бы видеть правильность
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(data)
