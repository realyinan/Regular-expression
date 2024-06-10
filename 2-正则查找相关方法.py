import re

# finditer返回的结果是一个可迭代对象
# findall把查找到的所有字符串结果放到一个列表里面
# fullmatch完整匹配
m1 = re.search(r'x', 'fsfhsdsdnfskxjxjiojxxjiojxxoji')
print(m1)
print('*'*100)

m2 = re.finditer(r'x', 'fsfhsdsdnfskxjxjiojxxjiojxxoji')
print(m2)
for i in m2:
    print(i)
print('*'*100)

m3 = re.findall(r'x\d+', 'fsfhsdsdnfskx34jx78jiojxxjiojxx4oji')
print(m3)
print('*'*100)

m4 = re.fullmatch(r'hello world', 'hello world')
print(m4)
print('*'*100)

m6 = re.fullmatch(r'h.*d', 'hello world')
print(m6)
