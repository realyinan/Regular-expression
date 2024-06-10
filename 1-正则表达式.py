import re

# 共同点: match 和s earch 方法只对字符串查询一次, 返回值类型都是re.Match对象.
# 不同点: match是从头开始匹配, 一旦匹配失败, 就返回None. search是在整个字符串里匹配

m1 = re.match(r'hello', 'hello hello world good morning')
print(m1)
print('*'*100)

m2 = re.search(r'hello', 'hello world good morning')
print(m2)
print('*'*100)

m3 = re.match(r'good', 'hello world good morning')
print(m3)
print('*'*100)

m4 = re.search(r'good', 'hello world good morning good')
print(m4)
print('*'*100)


