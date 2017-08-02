import requests


html=requests.get("https://api.douban.com/v2/movie/subject/1291546")
data=html.json()
print(data)