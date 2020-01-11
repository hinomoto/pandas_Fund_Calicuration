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

#カレントディレクトリ移動
   os.chdir(str(a))
   b.to_excel('pct_change.xlsx')

   b=a1.diff()
   b.to_excel('diff.xlsx')

#相関行列を出力します。
   b=a1.corr()
   b.to_excel('corr.xlsx')

#max,min等詳細データを出力します。
   b=a1.describe()
   b.to_excel('describe.xlsx')
   
####### 1Mリターン##########
#一旦 元のディレクトリに戻る
   os.chdir(path)

#1Mフォルダ移動&作成
   os.chdir(str(a))
   current = str(a)+"_1M"
   os.mkdir(current)

   c=a1.pct_change(freq='30D')   

#カレントディレクトリ移動
   os.chdir(current)
   c.to_excel('pct_change_1M.xlsx')

   b=c.diff()
   b.to_excel('diff_1M.xlsx')

   b=c.corr()
   b.to_excel('corr_1M.xlsx')

   b=c.describe()
   b.to_excel('describe_1M.xlsx')
   
####### 3Mリターン##########
#一旦 元のディレクトリに戻る
   os.chdir(path)

#1Mフォルダ移動&作成
   os.chdir(str(a))
   current = str(a)+"_3M"
   os.mkdir(current)

   c=a1.pct_change(freq='90D')   

#カレントディレクトリ移動
   os.chdir(current)
   c.to_excel('pct_change_3M.xlsx')

   b=c.diff()
   b.to_excel('diff_3M.xlsx')

   b=c.corr()
   b.to_excel('corr_3M.xlsx')

   b=c.describe()
   b.to_excel('describe_3M.xlsx')
   
####### 6Mリターン##########
#一旦 元のディレクトリに戻る
   os.chdir(path)

#1Mフォルダ移動&作成
   os.chdir(str(a))
   current = str(a)+"_6M"
   os.mkdir(current)

   c=a1.pct_change(freq='182D')   

#カレントディレクトリ移動
   os.chdir(current)
   c.to_excel('pct_change_6M.xlsx')

   b=c.diff()
   b.to_excel('diff_6M.xlsx')

   b=c.corr()
   b.to_excel('corr_6M.xlsx')

   b=c.describe()
   b.to_excel('describe_6M.xlsx')


####### 1Yリターン##########
#一旦 元のディレクトリに戻る
   os.chdir(path)

#1Mフォルダ移動&作成
   os.chdir(str(a))
   current = str(a)+"_1Y"
   os.mkdir(current)

   c=a1.pct_change(freq='365D')   

#カレントディレクトリ移動
   os.chdir(current)
   c.to_excel('pct_change_1Y.xlsx')

   b=c.diff()
   b.to_excel('diff_1Y.xlsx')

   b=c.corr()
   b.to_excel('corr_1Y.xlsx')

   b=c.describe()
   b.to_excel('describe_1Y.xlsx')   

#元のディレクトリに戻る
   os.chdir(path)
   num += 1

