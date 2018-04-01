import re
a=input().lower()
print(a)
b=[x for x in re.split('\W',a) if x]
print(b)
