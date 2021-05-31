# 何か質問するプログラムを書こう。入力された回答をファイルに書き出そう。

from os import write


anser = input("体重は？")

with open("challenge9_2.txt", "w", encoding="utf-8") as f:
    f.write(anser)