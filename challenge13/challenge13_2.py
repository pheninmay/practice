# Squareクラスにchange_sizeメソッドを定義して、そこに渡した数値の分だけSquareオブジェクト
# の横幅を増やしたり、減らしたり（マイナス値の場合）してみよう。

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square:
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, c):
        self.width += c

crec = Rectangle(7, 9)
csqu = Square(5)

print(crec.calculate_perimeter())
print(csqu.calculate_perimeter())

csqu.change_size(2)
print(csqu.calculate_perimeter())

csqu.change_size(-3)
print(csqu.calculate_perimeter())