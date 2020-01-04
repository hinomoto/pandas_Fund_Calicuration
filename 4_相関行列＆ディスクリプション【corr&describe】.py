import pandas as pd

df = pd.read_excel('data_henkango.xlsx', index_col=0)

a = df

#相関行列を出力します。
b=a.corr()
b.to_excel('corr.xlsx')

#max,min等詳細データを出力します。
c=a.describe()
c.to_excel('describe.xlsx')
