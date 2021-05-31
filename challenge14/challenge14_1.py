# Squareクラスにsquare_listクラス変数を追加しよう。そして、新しくSquareクラスのオブジェクトが
# 作られるたびに、そのオブジェクトをこのリストに追加しよう。

class Square:
    square_list = []
    def __init__(self, w):
        self.width = w
        self.square_list.append([self.width])

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, c):
        self.width = self.width + c

squ1 = Square(6)
squ2 = Square(75)
squ3 = Square(15)

print(Square.square_list)