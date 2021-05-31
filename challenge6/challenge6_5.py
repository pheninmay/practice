# リスト[”the”,”fox”,”jumped”,”over”,”the”,”fence”,”.”]の文字列を
# 正しい英文になるように連結しよう。単語と単語の間は空白が必要ですが
# 最後のピリオド前には空白は不要です。文字列を要素に持つリストを１つに
# 連結するメソッドがあることを忘れずに！

word_list = ["the","fox","jumped","over","the","fence","."]
print(word_list)

jword = " ".join(word_list[:6])
print(jword)

print(jword+word_list[6])