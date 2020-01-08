import pandas as pd
import os

#最初のディレクトリを取得
path = os.getcwd()

df = pd.read_excel('data_henkango.xlsx', index_col=0)

#開始する年度を入力してください
num = 1990

#終了する年度を入力してください。
while num < 2020:

   a=num
   print(df[df.index.year == a]) 
#print(df[df.index.year == 1990]) #1990年のみ抽出

#フォルダ作成
   os.mkdir(str(a))

#a1 新たにデータフレーム作成
   a1=df[df.index.year == a]

   b=a1.pct_change()
#b=a.pct_change(freq='2D')

#カレントディレクトリ移動
   os.chdir(str(a))
   b.to_excel('pct_change.xlsx')

   c=a1.diff()
   c.to_excel('diff.xlsx')

#相関行列を出力します。
   d=a1.corr()
   d.to_excel('corr.xlsx')

#max,min等詳細データを出力します。
   e=a1.describe()
   e.to_excel('describe.xlsx')
   
#1Mリターン
   f=a1.pct_change(freq='30D')
   f.to_excel('pct_change_1M.xlsx')

#3Mリターン
   g=a1.pct_change(freq='90D')
   g.to_excel('pct_change_3M.xlsx')


#6Mリターン
   h=a1.pct_change(freq='182D')
   h.to_excel('pct_change_6M.xlsx')

#1Yリターン
   i=a1.pct_change(freq='365D')
   i.to_excel('pct_change_1Y.xlsx')

#元のディレクトリに戻る
   os.chdir(path)
   num += 1

