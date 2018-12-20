from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")


# 找一个table便签, 并且id为giftList, 里面的'第一层的儿子们'
for child in bsObj.find("table", {"id": "giftList"}).children:  
    print(child)