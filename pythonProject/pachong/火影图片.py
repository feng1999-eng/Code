from lxml import etree
import requests
import os

url = 'https://wallhaven.cc/search?q=naruto'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
page_text = requests.get(url=url,headers=headers).text


tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="thumbs-container thumb-listing infinite-scroll"]/section/ul/li')
if not os.path.exists('./huoying'):
    os.mkdir('./huoying')
for li in li_list:
    img_src = li.xpath('./figure/img/@data-src')[0]
    img_name = li.xpath('./figure/@data-wallpaper-id')[0]
    img_data = requests.get(url=img_src,headers=headers).content
    img_path = './huoying/'+img_name+'.png'
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_src+"下载成功!")
