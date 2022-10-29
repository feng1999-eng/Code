import re

lst=re.findall(r"\d+","李金锋的电话：10010，吴冰冰的电话：10012")
print(lst)

s1=re.search(r"\d+","李金锋的电话：10010，吴冰冰的电话：10012")
print(s1)