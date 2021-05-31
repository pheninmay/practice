# メソッドを使って”Hemingway”の中で最初に”m”が出現するインデックスを調べよう

search = input("探したい文字を入力してください")
try:
    print("Hemingway".index(search))
except:
    print("Not Found")