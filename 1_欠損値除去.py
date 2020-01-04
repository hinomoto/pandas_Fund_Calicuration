import pandas as pd


#データフレームに格納
df = pd.read_excel('bloombergデータ.xlsm')

#print(df)


#全ての欠損値を削除
b=df.dropna(how='all')

#変換実行。”index=False”でindexを不要としている。

b.to_excel('data_henkango.xlsx', index=False)
#b.to_csv('data_henkango.csv', index=False)