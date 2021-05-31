# 六角形を表すHexagonクラスを定義しよう。そのクラスには外周の長さを計算して
# 返すメソッドcalculate_perimeterを定義しよう。そしてHexagonオブジェクトを
# 作ってcalculate_perimeterメソッドを呼び出し結果を出力しよう。

class Hexagon:
    def __init__(self, l1, l2, l3 ,l4 ,l5 ,l6):
        self.line1 = l1
        self.line2 = l2
        self.line3 = l3
        self.line4 = l4
        self.line5 = l5
        self.line6 = l6

    def calculate_perimeter(self):
        return self.line1 + self.line2 + self.line3 + self.line4 + self.line5 + self.line6

hexa = Hexagon(5, 4, 6, 7, 3, 4)
print(hexa.calculate_perimeter())