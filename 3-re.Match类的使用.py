import re

m = re.search(r'm.*j', 'fwimfjoiwjm')
print(m)
print('*'*100)

# 返回搜索开始的索引, 返回搜索结束的索引
print(m.pos, m.endpos)  
print('*'*100)

# 返回一个元组，包含匹配的子组在原字符串中的起始和结束位置。
print(m.span())  
print('*'*100)

# 使用group获取匹配的字符串结果
# group可以传参, 表示第 n 个分组
# 正则表达式中使用 () 表示一个分组, 其中(?P<name>表达式)给一个分组起名
# 如果没有分组, 默认只有一组
# 分组的下标从 0 开始
m1 = re.search(r'(?P<a>4.*)(?P<b>4.*)(?P<c>4.*2)', 'fhu4idhg4hghga4io2ghi')
print(m1)
print(m1.group())  # 匹配的字符串
print(m1.group(1))  # 第一个子组
print(m1.group(2))  # 第二个子组
print(m1.group(3))  # 第二个子组
print(m1.groups())  # 所有子组
print(m1.group('a'))
print('*'*100)
print(m1.groupdict())  # 返回一个包含所有命名组的字典。
print(m1.span(2))
print(m1.span('c'))