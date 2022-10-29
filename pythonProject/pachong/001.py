import requests
from bs4 import BeautifulSoup
import json
import prettytable as pt

singer_name = input("输入查找的歌手名：")
resp = requests.get("https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w=" + singer_name)

json_str = resp.text
json_dict = json.loads(json_str[9:-1])
song_list = json_dict['data']['song']['list']
table = pt.PrettyTable()
table.field_names = ['序号', '歌手', '歌曲', '专辑']
index = 0
for song in song_list:
    songname = song['songname']
    albumname = song['albumname']
    singer = song['singer'][0]['name']
    table.add_row([index, singer, songname, albumname])
    index += 1
print(table)
