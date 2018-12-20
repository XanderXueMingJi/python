from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class": "green"})  # 找到span标签并且class为green
print('nameList:', nameList)
for name in nameList:
    print(name.get_text())  # get_text  获取标签里面的内容