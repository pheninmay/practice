# コンピューターにあるなにかのファイルをPythonで開いて
# コンテンツを出力しよう

import os

filename = os.path.join("C:" + os.sep, "Users", "pheni", "OneDrive", "デスクトップ", "result2.txt")

with open(filename, "r", encoding="utf-8") as f:
    print(f.read())