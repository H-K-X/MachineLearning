import pandas as pd
import numpy as np

def cutline():
    print('--------------------')

s = pd.Series([10, 30, 40], index=[1,3,4])
print(s)
cutline()

s.loc[2] = np.nan
s.sort_index(inplace=True)
s.interpolate(method='index', inplace=True)  # 插值补全
print(s)  # 删除指定标签的行，返回新对象，原 s 不变
cutline()
