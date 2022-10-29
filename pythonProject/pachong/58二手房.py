from lxml import etree
import requests

if __name__ == "__main__":
    url = 'https://www.sohu.com/a/398205958_373007'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    r = tree.xpath('//div[@class="text"]/article/p')
    fp = open('三国人物介绍.txt','w',encoding='utf-8')
    for p in r:
        content = p.text
        if(content!=None):
            fp.write(content+'\n')

    print("爬取完成！！！")

