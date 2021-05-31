# 数字を入力値として受け取り、その数字を２乗した戻り値を返す関数を書いてみよう

def double_pow():
    """
    Print n * n.
    :param n: int.
    :return: power of n to print.
    """
    n = input("数値を入力してください")
    n =int(n)
    print(n * n)

double_pow()