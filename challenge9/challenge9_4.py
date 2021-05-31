# チャレンジ３を日本語で同じ様にやってみよう。例えば、"Top Gun"を”トップガン”のように
# 日本語に置き換えてCSVファイルに書き出そう。

import csv

japanese_title = [["トップガン", "卒業白書", "マイノリティーリポート"],
                  ["タイタニック", "レヴェナント: 蘇えりし者", "インセプション"],
                  ["トレーニングデイ", "マイ・ボディガード", "フライト"]
                 ]

with open("challenge9_4.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for i in japanese_title:
        w.writerow(i)