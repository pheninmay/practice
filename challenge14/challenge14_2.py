# Squareクラスのオブジェクトをprint関数に渡したら、４辺それぞれの
# 長さを出力しよう。たとえば、Square(29)のようにオブジェクトを作ったら
# print関数では29 by 29 by 29 by 29と出力しよう。

class Square:
    square_list = []
    def __init__(self, w):
        self.width = w
        self.square_list.append([self.width])

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, c):
        self.width = self.width + c

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width,)

psqu = Square(50)
print(psqu)