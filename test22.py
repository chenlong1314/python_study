import requests
from bs4 import BeautifulSoup
import re

r=requests.get("https://movie.douban.com/review/8687473/")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
hh=soup.find_all('p')
for item in hh:
    print(item.string)

hh_s=re.compile('<button class="btn useful_count 8687473 "> (...*?)</button>')
p=re.findall(hh_s,demo)
print(p)


