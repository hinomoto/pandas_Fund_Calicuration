import pandas as pd
import os

#最初のディレクトリを取得
path = os.getcwd()


#開始する年度を入力してください
num = 1990

#リストlを作成
l = list(range(0))

#リストlを作成
l2 = list(range(0))     

#変数列iに●を入力
i=6

#変数行jに●を入力
j=2

#ファイル名入力
file='corr.xlsx'

#終了する年度を入力してください。
while num < 2020:
   a=num
   
   #print(df[df.index.year == a]) 
   
   os.chdir(path)
   os.chdir(str(a))
   df = pd.read_excel(file, index_col=0)
   
#index(列）の名前を取得 する場合 print(df.index[1])
   
  
#aに年度を入力。listに追加
   l.append(a)
   print(l)
   
#bに値（2列目0行等）を入力。listに追加
   
   b=df.iat[i,j]
   l2.append(b)
   print(l2)   
   print(df.columns[i])      
   num += 1


#元のディレクトリに一旦戻る
os.chdir(path)

#データフレームに入力する
hino=pd.DataFrame(l)

#df.columns[2]→column indexの2列目という列を作成してl2リストデータの列を追加
hino[df.columns[i]]=pd.DataFrame(l2)
hino.to_excel(df.index[j]+'&'+df.columns[i]+'.xlsx')

