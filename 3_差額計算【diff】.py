import pandas as pd

df = pd.read_excel('data_henkango.xlsx', index_col=0)

a = df

b=a.diff()
b.to_excel('diff.xlsx')


