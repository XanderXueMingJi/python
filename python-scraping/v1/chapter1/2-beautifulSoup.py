from urllib.request import urlopen
from bs4 import BeautifulSoup  # 需要安装  控制台执行 pip install beautifulsoup4

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)
