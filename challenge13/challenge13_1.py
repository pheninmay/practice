# RectangleとSquareクラスを作ろう。両方のクラスに、その図形の外周の長さを計算して返す
# calculate_perimeterメソッドを定義しよう。そして、RectangleとSquareのオブジェクトを
# 作って、それぞれのcalculate_perimeterメソッドを呼ぼう。

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

crec = Rectangle(7, 9)
csqu = Square(5)

print(crec.calculate_perimeter())
print(csqu.calculate_perimeter())