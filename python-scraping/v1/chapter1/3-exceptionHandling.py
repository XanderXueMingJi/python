from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# import sys


def getTitle(url):
    try:
        html = urlopen(url)  # 打开网站
        print('html:', html)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        print('bsObj:', bsObj)
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title is None:  # if title == None:
    print("Title could not be found")
else:
    print(title)
