# 変数が１０以下だったらメッセージを出力しよう。１０より大きく２５以下だったら
# 別のメッセージを出力しよう。２５より大きかったら更に別のメッセージを出力しよう。

x=10

if x<=10:
    print("xは１０以下です")
elif x>10 and x<=25:
    print("xは１０より大きく２５以下です")
else:
    print("xは２６以上です")