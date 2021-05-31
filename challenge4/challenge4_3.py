# ３つの必須引数と２つのオプション引数がある関数を書いてみよう

def five_opt(x,y,z,a=35,b=40):
    """
    return x+y+z+a+b.
    :param x: int req.
    :param y: int req.
    :param z: int req.
    :param a: int opt(35).
    :param b: int opt(40).
    :return: sum of x and y,z,a,b
    """
    return x+y+z+a+b

print(five_opt(1,2,3))