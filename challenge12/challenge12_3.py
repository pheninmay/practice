# 三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。そしてTriangle
# オブジェクトを作って、areaメソッドを呼び出して、結果を出力しよう。

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2

tri = Triangle(10, 6)
print(tri.area())