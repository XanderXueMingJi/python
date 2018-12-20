from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")


# 找一个table便签, 并且id为giftList, 里面的'第一层的儿子们' 不要找到第一个儿子
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings: 
    print(sibling) 