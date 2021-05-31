# 変数ageに整数を代入し、そのageを使って何かしらの条件分岐をして
# 条件に応じてメッセージを出力しよう

age=5

if age < 3:
    print("保育園")
elif age < 6:
    print("保育園、幼稚園")
elif age < 12:
    print("小学校")
elif age < 15:
    print("中学校")
elif age < 18:
    print("高校")
elif age < 22:
    print("大学")
else:
    print("社会人")