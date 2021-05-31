# りんごと言われて思い浮かぶ、４つの属性を考えよう。その４つの属性を
# インスタンス変数に持つ、Appleクラスを定義しよう。

class Apple:
    def __init__(self, w, c, sw, so):
        self.weight = w
        self.color = c
        self.sweetness = sw
        self.sour = so
        print("作成しました")

ap = Apple(100, "red", 6, 3)
print(ap.weight, ap.color, ap.sweetness, ap.sour)