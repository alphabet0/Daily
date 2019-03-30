# import pandas as pd
# import numpy as np
# path='C:\\Users\wy610\OneDrive\Documents\统计/上课时间与番茄时的关系.xlsx'
# data=pd.read_excel(path)
# # print(data)
# for index,groups in data.groupby('受控制时间'):
#     # print(groups)
#     print(groups['番茄个数'].sum())


# 46 335
# 7.64
def evaluate_time():
    per=335/46
    need=7.64*1024
    time=need/per
    already=3.2*1024
    dotime=already/per
    print(dotime)
    print(time)


