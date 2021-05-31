# 円を表すCircleクラスを定義しよう。そのクラスに面積を計算して返すメソッドareaを持たせよう。
# 面積の計算には、Pythonの組み込みモジュールMathのpi定数が使えます。次に、Circleオブジェクト
# を作って、areaメソッドを呼び出し、結果を出力しよう

import math

class Circle:
    def __init__(self, d):
        self.diameter = d
        self.radius = d / 2

    def area(self):
        return self.radius ** 2 * math.pi

ci = Circle(8)
print(ci.area())