from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

#  找到一个图片src属性为"../img/gifts/img1.jpg"
jpg = bsObj.find("img", {"src": "../img/gifts/img1.jpg"})

#  图片的父标签的前一个兄弟的内容
text = jpg.parent.previous_sibling.get_text()
print(text)
