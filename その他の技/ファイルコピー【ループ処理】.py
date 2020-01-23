import pandas as pd
import os
import shutil


#最初のディレクトリを取得
path = os.getcwd()

list=['1Y','5Y','10Y','15Y','20Y','30Y','40Y']

print(list)

for i in list:
   #●Yディレクトリ移動
   os.chdir(str(path))
   shutil.copy('./'+ str(i) +'/price(Bond&IRS)hinogeneric'+ str(i) +'.xlsx', './ファイル結合/'+str(i)+'.xlsx')
   
   
   