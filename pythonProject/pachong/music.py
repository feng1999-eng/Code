from bs4 import BeautifulSoup
import requests
import re

url = "https://www.9ku.com/music/"
resp = requests.get(url)

page = BeautifulSoup(resp.text, "html.parser")
ol = page.find("ol", attrs={"id": "f1",
                            })
lis = ol.find_all("li")
print(lis)
