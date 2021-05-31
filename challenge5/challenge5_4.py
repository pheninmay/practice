# 任意のキーを入力させるプログラムを書こう。入力されたキーを使って
# １つ前のチャレンジで用意した辞書から、バリューを取得して表示しよう

my_characters = {"1": "121cm",
                 "2": "48kg",
                 "3": "Blue"}

key = input("数字を入力してください。")
if key in my_characters:
    print(my_characters[key])
else:
    print("見つかりません")