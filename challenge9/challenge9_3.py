# リストのリストに含まれている要素をCSVファイルに書き出そう。データは次の通り:
# [["Top Gun", "Risky Business", "Minority Report"],
#  ["Titanic", "The Revenant", "Inception"],
#  ["Traning Day", "Man of Fire", "Flight"]
# ]
# データの各要素はCSVの１行となり、その１行に含まれる各要素がカンマで区切られるように書き出そう。

import csv

title = [["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Traning Day", "Man of Fire", "Flight"]
        ]

with open("challenge9_3.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for i in title:
        w.writerow(i)