from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


# random.seed 随机数据可预测
# datetime.datetime.now(): 2018-12-20 14:07:03.648431
random.seed(datetime.datetime.now())  # None

#  进入爬虫状态了


def getLinks(articleUrl):

    #  https://en.wikipedia.org/wiki/Kevin_Bacon  维基百科 这次介绍人
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {
        "id": "bodyContent"
    }).findAll(
        "a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
print('links:', links)
while len(links) > 0:

    # random.randint随机数
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]  
    print(newArticle)
    links = getLinks(newArticle)