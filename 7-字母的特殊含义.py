import re

# \n: 表示换行 \t: 表示一个制表符 \s: 空白字符 \S: 非空白字符

# \d 表示数字 等价于[0-9]
print(re.search(r'x\d+p', 'x233p'))
print('*'*100)

# \D 表示非数字 等价于[^0-9]
print(re.search(r'\D+', 'he110'))
print('*'*100)

# \w 表示数字,字母,下划线 等价于[0-9a-zA-Z_]
print(re.findall(r'\w+', 'h+e11_0*^23-@'))
print(re.findall(r'\w+', '大,家+好'))
print('*'*100)

# \W 表示非数字,字母,下划线 等价于[^0-9a-zA-Z_]
print(re.findall(r'\W+', 'h+e11_0*^23-@'))