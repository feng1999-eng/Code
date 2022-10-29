import re  # 正则表达式
import urllib.error
import urllib.request
import xlwt  # Excel
import requests
from bs4 import BeautifulSoup
import sqlite3


def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # 定义爬取网页
    datalist = getData(baseurl)
    # savepath = "豆瓣电影Top250.xls"
    # saveData(datalist, savepath)
    dbpath = "movie250.db"
    saveData_db(datalist, dbpath)


# 电影详情页
findlink = re.compile(r'<a href="(.*?)">')
# 电影封面
Imagelink = re.compile(r'<img.*src="(.*?)".*', re.S)

# 电影名称
Titlelink = re.compile(r'<span class="title">(.*)</span>')

# 评分
Scorelink =re.compile(r'<span class="rating_num".*>(.*?)</span>')

#评价人数
Peoplelink = re.compile(r'<span>(\d*)人评价</span>')

#简介
Contentlink = re.compile(r'<span class="inq">(.*?)</span>')

def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askurl(url)
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            Link = re.findall(findlink, item)[0]
            Image = re.findall(Imagelink, item)[0]
            Title = re.findall(Titlelink, item)
            Score = re.findall(Scorelink, item)[0]
            People = re.findall(Peoplelink, item)[0]
            Content = re.findall(Contentlink, item)
            if len(Content) == 1:
                Content = Content[0]
            else:
                Content = ""
            data.append(Link)
            data.append(Image)
            if len(Title) == 2:
                Chinese_title = Title[0]
                data.append(Chinese_title)
                English_title = Title[1].replace("/", "")
                data.append(English_title)
            else:
                data.append(Title[0])
                data.append(' ')
            data.append(Score)
            data.append(People)
            data.append(Content)
            datalist.append(data)
    return datalist


def askurl(url):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 106.0.0.0Safari / 537.36'
    }
    requests = urllib.request.Request(url=url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(requests)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist, savepath):
    print("正在saving....")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "封面链接", "电影中文名", "电影外文名", "电影评分", "评价人数", "电影简介")
    for i in range(0, 7):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("正在读取第%d" % (i + 1))
        data = datalist[i]
        for j in range(0, 7):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


def saveData_db(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250(
                    info_link,pic_link,cname,oname,score,people,content)
                    values(%s)''' % ','.join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            oname varchar,
            score numeric ,
            people numeric ,
            content text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    print("搞定")
