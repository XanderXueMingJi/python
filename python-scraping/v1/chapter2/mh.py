from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://99770.hhxxee.com/comic/25146/325240/")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("body")  # 找到span标签并且class为green
print('nameList:', nameList)
for name in nameList:
    print(name.get_text()) 