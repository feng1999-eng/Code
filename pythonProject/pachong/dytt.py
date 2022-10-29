import requests
import re

url = "https://www.dydytt.net/"
url1 = "https://www.dydytt.net/index2.htm"
resp = requests.get(url1)
resp.encoding = 'gb2312'
print(resp.text)

obj1 = re.compile(r"最新电影更新.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)

result1 = obj1.finditer(resp.text)

for it in result1:
    ul = it.group('ul')

result2 = obj2.finditer(ul)
for itt in result2:
    href = itt.group('href')
    print(url+href)
