#利用方法 
#①同じディレクトリに（極力同じ形式）のファイルを入れる。（ファイル名は何でもOK）
#②このpyファイルを実行。自動でマージされるはず。

import json

import pandas as pd

import glob


excel_files = glob.glob('*.xlsx')

list = []

for f in excel_files:

    list.append(pd.read_excel(f))

df = pd.concat(list)


df.to_excel("TOTAL.xlsx")
