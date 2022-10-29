from lxml import etree
import requests

url = "https://nba.stats.qq.com/stats/detail/?order=defen&type=player"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

page_text = requests.get(url=url, headers=header).text

r = etree.HTML(page_text)
li_list = r.xpath('//div/ul[@class="content"]/ul/li/span[@class="qiuyuan"]')
for li in li_list:
    name = li.text
    print(name)



