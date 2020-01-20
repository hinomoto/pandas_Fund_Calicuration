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


#終了する年度を入力してください。
while num < 2020:
   a=num
   
   #print(df[df.index.year == a]) 
   os.chdir(path)
   os.chdir(str(a))
   df = pd.read_excel('corr.xlsx', index_col=0)
   
#index(列）の名前を取得   
   print(df.index[1])
  
#aに年度を入力。listに追加

   l.append(a)
   print(l)
   
#bに値（2列目0行等）を入力。listに追加
   b=df.iat[2,0]
   l2.append(b)
   print(l2)
   
   print(df.columns[2])
   num += 1

#元のディレクトリに一旦戻る
os.chdir(path)

#データフレームに入力する
hino=pd.DataFrame(l)


#df.columns[2]→column indexの2列目という列を作成してl2リストデータの列を追加
hino[df.columns[2]]=pd.DataFrame(l2)
hino.to_excel(df.index[1]+'&'+df.columns[2]+'.xlsx')
