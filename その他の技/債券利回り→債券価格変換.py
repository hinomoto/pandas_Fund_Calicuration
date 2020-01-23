import pandas as pd
import os

#最初のディレクトリを取得
path = os.getcwd()

df = pd.read_excel('data_henkango.xlsx', index_col=0)

#例 df['D'] = df['GTJPY1Y Govt'] / 100 
#** はべき乗。100/(1+(利回り/100))^1年

year = 10

df= 100/(1+(df/100))**year
print(df)


df.to_excel('price(Bond&IRS)hinogeneric'+str(year)+'Y.xlsx')