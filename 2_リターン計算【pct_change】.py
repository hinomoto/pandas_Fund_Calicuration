import pandas as pd

df = pd.read_excel('data_henkango.xlsx', index_col=0)

a = df

b=a.pct_change()

###  "b=a.pct_change(freq='2D')" →2日間のリターン
###  "b=a.pct_change(freq='1w')" →1週間のリターン
###  "b=a.pct_change(freq='1M')" →1か月リターン


b.to_excel('pct_change.xlsx')




