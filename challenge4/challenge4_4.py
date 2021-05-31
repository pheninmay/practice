# ２つの引数からなるプログラムを書いてみよう。１つ目の関数は整数を引数として受け取り
# その整数を２で割って求められる整数を出力として返そう。２つ目の関数は整数を引数として
# 受け取り、４でかけた整数を返そう。プログラム内で、１つ目の関数を呼び、戻り値を変数
# として保存し、２つ目の関数の引数として渡そう

def two_div(x):
    """
    return x // 2
    :param x: int
    :return: 2 div of x
    """
    return x // 2

def four_multi(x):
    """
    return x * 4
    :param x: two_div return value
    :return: 4 multi of x
    """
    return x * 4

result = two_div(5)
print(four_multi(result))