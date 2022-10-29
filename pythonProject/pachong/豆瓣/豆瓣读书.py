import requests
from bs4 import BeautifulSoup
import re
import MySQLdb
import time

findTitle = re.compile(r'<a href=.*?title="(.*?)">', re.S)
findAuthor = re.compile(r'<p class="pl">(.*?)/')
findSocre = re.compile(r'<span class="rating_nums">(.*?)</span>')
findPeople = re.compile(r'<span class="pl">(.*?)</span>', re.S)
findImage = re.compile(r'img src="(.*?)" width="90"')
findContent = re.compile(r'<span class="inq">(.*?)</span>')


def main():
    baseurl = 'https://book.douban.com/top250?start='
    datalist = []
    datalist = getData(baseurl)
    # savePath = "book250.db"
    # saveBook(datalist, savePath)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        data = askurl(url)
        datalist.append(data)
    return datalist


def askurl(url):
    headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 106.0.0.0Safari / 537.36'
    }
    proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
    response = requests.get(url=url, headers=headers, proxies=proxies)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    tr_list = soup.find_all('tr', class_="item")
    data = []
    for tr in tr_list:
        data_tr = []
        title = re.findall(findTitle, str(tr))[0]
        author = re.findall(findAuthor, str(tr))[0]
        score = re.findall(findSocre, str(tr))[0]
        people = re.findall(findPeople, str(tr))[0]
        people = people.replace('\n', '')
        people = re.findall(r'[0-9]*', people)[21]
        Image = re.findall(findImage, str(tr))[0]
        content = re.findall(findContent, str(tr))
        data_tr.append(title)
        data_tr.append(author)
        data_tr.append(score)
        data_tr.append(people)
        print(Image)
        if len(content) == 0:
            data_tr.append('')
        else:
            data_tr.append(content[0])
        data.append(data_tr)
    return data


def initDb(savePath):
    sql = '''
            create table book250
            (
                id integer primary key auto_increment,
                title varchar,
                author varchar,
                score numeric,
                people numeric,
                content text
                )
    '''
    conn = MySQLdb.connect("localhost", "root", "990701", "MyBlog", charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def saveBook(datalist, savePath):
    initDb(savePath)
    conn = MySQLdb.connect("localhost", "root", "990701", "MyBlog", charset="utf8")
    cursor = conn.cursor()   
    for data_tr in datalist:
        for data in data_tr:
            for index in range(len(data)):
                if index == 2 or index == 3:
                    continue
                data[index] = '"' + str(data[index]) + '"'
            sql = '''
                insert into book250(
                    title,author,score,people,content)
                    values 
                    (%s)''' % ','.join(data)
            cursor.execute(sql)
            conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    time_cost = end - start
    print("爬取成功,用时" + f'{time_cost}' + "秒")
