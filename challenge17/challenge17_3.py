# Pythonのreモジュールを使って、何かの文字の後にoが２回登場する単語に一致する正規表現を書こう。
# そして、"The ghost that says boo haunts the loo"の文中にあるbooやtooに一致するか試そう。

import re

example = "The ghost that says boo haunts the loo"
m = re.findall(".oo", example)
print(m)