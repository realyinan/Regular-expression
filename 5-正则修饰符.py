import re
# 正则修饰符是对正则表达式进行修饰

# re.S 使'.'匹配包括换行符在内的所有字符。
m = re.search(r'm.*a', 'adaadamfw\nfwifafjsofa', flags=re.S)
print(m)
print('*'*100)

# re.I 忽略大小写。匹配时不区分大小写。
m1 = re.search(r'x', 'good Xyz', flags=re.I)
print(m1)
print('*'*100)

# re.M 使 ^ 和 $ 匹配每一行的开头和结尾，而不仅仅是整个字符串的开头和结尾
m2 = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)
print(m2)