import pandas as pd


#EXCELorCSVをインポート。データフレームに格納。 NA があるデータでも可
df = pd.read_excel('●●.xlsm')
#df = pd.read_csv('●●.csv')


#全ての欠損値を削除
b=df.dropna(how='all')

#変換実行。”index=False”でindexを不要としている。

b.to_excel('data_henkango.xlsx', index=False)
#b.to_csv('data_henkango.csv', index=False)