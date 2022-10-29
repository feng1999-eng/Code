import requests
import urllib3
from bs4 import BeautifulSoup
import parsel
import os

for i in range(1, 10):

    url = 'https://www.kanxiaojiejie.com/i/category/xiaotianmei/page/' + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    urllib3.disable_warnings()
    proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
    resp = requests.get(url=url, headers=headers, verify=False, proxies=proxies)
    selector = parsel.Selector(resp.text)
    url_list = selector.css('.entry-title > a::attr(href)').getall()
    title_list = selector.css('.entry-title > a::text').getall()

    for zip_data in zip(url_list, title_list):
        url1 = zip_data[0]
        title = zip_data[1]
        resp1 = requests.get(url=url1, proxies=proxies)
        data_html1 = resp1.text
        selector1 = parsel.Selector(data_html1)
        img_list = selector1.css('div.entry-content > div > p > img::attr(src)').getall()
        for img_url in img_list:
            img_data = requests.get(url=img_url, proxies=proxies).content
            img_name = img_url.split('/')[-1]
            with open("img\\" + img_name, mode='wb') as f:
                f.write(img_data)
            print(img_name, "爬取成功")
