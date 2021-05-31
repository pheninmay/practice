# Shapeクラスを定義しよう。呼ばれたら”I am a shape”を返すメソッドwhat_am_iを定義しよう。
# 前のチャレンジで定義したRectangleとSquareクラスを変更して、このShapeクラスを継承させよう。
# そして、RectangleとSquareのオブジェクトを生成して、このチャレンジで追加した
# メソッドwhat_am_iを呼んでみよう。

class shape:
    def what_am_i(self):
        return "I am a shape"

class Rectangle(shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(shape):
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, c):
        self.width = self.width + c

srec = Rectangle(7, 44)
ssqu = Square(7)

print(srec.what_am_i())
print(ssqu.what_am_i())