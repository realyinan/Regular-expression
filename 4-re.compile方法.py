import re

r = re.compile(r'o.*o')

x = r.search('iosdvos')
print(x)