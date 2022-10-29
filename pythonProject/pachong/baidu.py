import requests
from lxml import etree

url = "http://www.baidu.com"
resp = requests.get(url)
resp.encoding="utf-8"

html = etree.HTML(resp.text)
#获取所有a标签的href属性
linklist = html.xpath("//a/@href")

for item in linklist:
    print(item)