import re
# \s 匹配任何空白字符，包括空格、制表符、换页符等等 [\f\n\r\t\v]
print(re.search(r'\s', 'hello world'))
print(re.search(r'\s', 'hello\nworld'))
print(re.search(r'\s', 'hello\tworld'))
print('*'*100)

# \S 匹配任何非空白字符。等价于[^\f\n\r\t\v]
print(re.search(r'\S', '\t\n   x'))
print('*'*100)

# 标点符号的作用
# (): 用来表示一个分组
m = re.search(r'h(\d+)x', 'sh829xkflsa')
print(m.group(1))
m1 = re.search(r'\(.*\)', '(1+1)*3')
print(m1.group())
print('*'*100)

# . :表示匹配除了换行以外的任意字符.如果想要匹配 . , \.

# [] : 表示表示可选项
print(re.search(r'f[0-8]m', 'adaf8m'))
print(re.search(r'f[a-z]m', 'adafsm'))
print(re.search(r'f[0-5]+m', 'adaf1235m'))
print(re.search(r'f[0-9a-z]+m', 'adaf1235ewm'))
print('*'*100)

# | 表示或者
print(re.search(r'(x|p|t|d)m', 'pdfsdm'))
print('*'*100)

# {} 用来规定前面元素出现的次数
# {n} 表示前面的元素出现 n 次
# {n,} 表示前面的元素出现 n 次以上
# {,n} 表示前面的元素出现 n 次以下
# {n,m} 表示前面的元素出现 n-m 次
print(re.search(r'go{2}d', 'good'))
print(re.search(r'go{2,}d', 'goood'))
print(re.search(r'go{,2}d', 'gd'))
print(re.search(r'go{,2}d', 'god'))
print(re.search(r'go{,2}d', 'good'))
print(re.search(r'go{3,5}d', 'goood'))
print(re.search(r'go{3,5}d', 'gooood'))
print('*'*100)


# * 表示前面的元素出现任意次数等价于 {0,} 
print(re.search(r'go*d', 'gd'))
print(re.search(r'go*d', 'god'))
print('*'*100)

# + 表示前面的元素至少出现一次等价于 {1,}
print(re.search(r'go+d', 'god'))
print(re.search(r'go+d', 'gd'))
print(re.search(r'go+d', 'good'))
print('*'*100)

# ? 表示前面的元素最多只能出现一次, 等价于 {,1}
print(re.search(r'go?d', 'god'))
print(re.search(r'go?d', 'gd'))
print(re.search(r'go?d', 'good'))
print('*'*100)

# ^以指定的内容开头 $以指定的内容结尾
print(re.search(r'^a.*i$', 'afsfsfgjsi')) 











