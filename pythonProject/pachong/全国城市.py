from lxml import etree
import requests

url = "https://www.aqistudy.cn/historydata/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list1 = tree.xpath('//div[@class="hot"]//li')
fp = open('城市.txt','w',encoding='gb2312')
fp.write("热门城市:"+'\n')
for li in li_list1:
    name = li.xpath('./a/text()')[0]
    fp.write(name+'   ')
fp.write('\n')
ul_list = tree.xpath('//div[@class="bottom"]/ul')
fp.write("全部城市:")
for ul in ul_list:
    li_list2 = ul.xpath('./div[2]/li')
    title = ul.xpath('./div[1]/b/text').extract[0]
    print(title)
    for li in li_list2:
        name = li.xpath('./a/text()')[0]
        fp.write(name+'   ')
    fp.write('\n')
print("爬取完成！！")
fp.close()