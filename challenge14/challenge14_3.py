# ２つのパラメーターを受け取る関数を書こう。この関数は同じオブジェクトを渡されたら
# Trueを返し、そうじゃなかったらFalseを返そう。

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

def object_compare(obj1, obj2):
    return obj1 is obj2

squ1 = Square(34)
squ2 = Square(66)
same_squ = squ1

print(object_compare(squ1, same_squ))