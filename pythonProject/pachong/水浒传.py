import requests
from lxml import etree

url = "https://www.shicimingju.com/book/shuihuzhuan.html"
headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
page = requests.get(url=url,headers=headers)
page.encoding='utf-8'
page_text = page.text

tree = etree.HTML(page_text)
r = tree.xpath('//div[@class="book-mulu"]/ul/li/a')
fp = open("水浒传.txt",'w',encoding='utf-8')
for a in r:
    content = a.text
    detail_url = a.xpath('/a/@href')
    print(detail_url)
    fp.write(content+'\n')

fp.close()
print("爬取成功！！！")

