# ２つの文字列を入力させるプログラムを書こう。
# その文字列をそれぞれ別の文字列の２つの箇所に穴埋めした新しい文字列を作ろう。
# ”私は昨日[入力１]を書いて、[入力２]に送った！”
# そしてそれを出力しよう。

i1 = input("何を？")
i2 = input("誰に？")

r = "私は昨日{}を書いて、{}に送った！".format(i1,i2)
print(r)