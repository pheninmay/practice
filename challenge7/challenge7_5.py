# ２つのリストに含まれるすべての数字の組み合わせで掛け算しよう。
# １つ目のリストは[8, 19, 148, 4]、２つ目のリストは[9, 1, 33, 83]
# で、それぞれ掛け算した結果は新しいリストに格納しよう。

lis1 = [8, 19, 148, 4]
lis2 = [9, 1, 33, 83]
result = []

for i in lis1:
    for j in lis2:
        result.append(i*j)

print("{}{}".format(len(result),(result)))