import re
import xlwt
from bs4 import BeautifulSoup
import requests

baseurl = 'https://nba.hupu.com/players/'
play_list = ['russellwestbrook-3016.html', 'lebronjames-650.html', 'anthonydavis-3638.html','stephencurry-3311.html']
datalist = []
data_find = re.compile(r'<td.*?>(.*?)</td>')
headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 106.0.0.0Safari / 537.36'
}

getname = re.compile(r'<h2>(.*?)<p.*</h2>', re.S)
getImage = re.compile(r'<img src="(.*?)"/>')
getInfo = re.compile(r'<p>(.*?)</p>', re.S)
getTeam = re.compile(r'<a href.*title=".*">(.*?)</a>')
for player in play_list:
    play_data = []
    url = baseurl + player
    response = requests.get(headers=headers, url=url)
    response.encoding = 'utf-8'
    page_text = response.text
    soup = BeautifulSoup(page_text, 'html.parser')
    team_data = soup.find('div', class_="team_data")
    team_data = str(team_data)
    name = re.findall(getname, team_data)[0].replace('\n', '')
    play_data.append(name)
    Image_div = soup.find('div', class_="img")
    Image = re.findall(getImage, str(Image_div))[0]
    play_data.append(Image)
    Font_div = soup.find('div', class_="font")
    Info = re.findall(getInfo, str(Font_div))
    team_name = re.findall(getTeam, Info[4])[0]
    play_data.append(team_name)
    datalist.append(play_data)
print(datalist)
