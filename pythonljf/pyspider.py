import requests
import re
import time
import os

headers = {
    'Referer': 'https://t.cdn.ink/image',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.212 Safari/537.36 '
}
number_list = ['18766', '18745', '18710', '18723', '18618', '18640', '18566', '18488', '18447', '18161', '18006', '17949']
for num in number_list:
    ever_url = 'https://www.vmgirls.com/' + num + '.html'
    response = requests.get(url=ever_url, headers=headers)
    html = response.text
    dir_name = re.findall('<a rel=".*?" href="(.*?)" alt=".*?" title=".*?">', html)
    for url in dir_name:
        time.sleep(1)
        file_name = url.split('/')[-1]
        response = requests.get(url, headers=headers)
        path = 'd:\\爬虫图片001\\'
        with open(path + file_name, 'wb') as f:
            f.write(response.content)
            print("爬取" + file_name + "成功")
