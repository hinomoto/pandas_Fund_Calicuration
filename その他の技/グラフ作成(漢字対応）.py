import pandas as pd

import matplotlib as mpl

import matplotlib.pyplot as plt

#漢字対応"encoding="SHIFT-JIS" 
df=pd.read_excel('data_henkango.xlsx', encoding="SHIFT-JIS")

#"df.columns.values"にて列名取得＆list作成。

list=df.columns.values

num = 1

while num < 500:      

   #xにDATEcolumns[0]0列目y に列名を入力  

   df.plot(x=df.columns[0],y=df.columns[num])    

   plt.savefig(list[num]+".png")
      
   #plt.show()   

   num += 1