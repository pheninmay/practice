# チャレンジ１のリストの要素をそれぞれ、インデックス値と一緒に出力しよう

drama_title = ["ウォーキング・デッド",
                "アントラージュ",
                "ザ・ソプラノズ",
                "ヴァンパイア・ダイアリーズ"]

for i in range(len(drama_title)):
    print("{}{}".format(i,drama_title[i]))