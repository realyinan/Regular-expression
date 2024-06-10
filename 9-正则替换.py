import re

# 第一个参数是正则表达式
# 第二个参数是新字符或者一个函数
# 第三个参数是需要被替换的原来的字符串
print(re.sub(r'\d', 'x', 'fgjf34235621sdjgoig'))
print(re.sub(r'\d+', 'x', 'fgjf34235621sdjgoig'))
print(re.sub(r'\d', lambda x: str(int(x.group())*2), 'fgjf34235621sdjgoig'))
