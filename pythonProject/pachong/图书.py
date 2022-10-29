from lxml import etree
import requests

url = 'https://book.douban.com/latest?subcat=%E5%8E%86%E5%8F%B2%E6%96%87%E5%8C%96&p=1'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slide-list"]//li')
fp = open('./图书.txt','w',encoding="utf-8")
for li in li_list:
    title = li.xpath('./div[@class="info"]/div[@class="more-meta"]/h4/text()')[0].strip()
    name = li.xpath('./div[@class="info"]/div[@class="author"]/text()')[0].strip()
    fp.write(title+'   ')
    fp.write("作者"+name+'\n')
fp.close()
