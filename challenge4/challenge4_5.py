# 文字列をfloat型に変換して戻り値とする関数を書いてみよう。
# 起こり得る例外をキャッチする例外処理を書こう

def str_to_float(x):
    """
    return float(x)
    :param x: number str
    :return: float
    """
    try:
        return float(x)
    except ValueError:
        return "数字ではありません"

try:
    print(str_to_float("数字です"))
except NameError:
    print("未定義の引数です")