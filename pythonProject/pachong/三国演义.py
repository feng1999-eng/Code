
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    page = requests.get(url=url,headers=headers)
    page.encoding = 'utf-8'
    page_text =page.text
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul >li')
    fp = open('./sanguoyanyi.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = "http://www.shicimingju.com" + li.a['href']
        detail_page = requests.get(url=detail_url,headers=headers)
        detail_page.encoding = 'uft-8'
        detail_page_text = detail_page.text
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write(title+":"+content+'\n')
        print(title+"爬取成功！")