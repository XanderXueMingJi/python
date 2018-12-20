from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
allText = bsObj.findAll(id="text")
print('allText:', allText)
print(allText[0].get_text())  # 因为id名也可能重复,  所以用数组