from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()  # 注释了也能正常运行
random.seed(datetime.datetime.now()) # 注释了也能正常运行


# 检索在页面上找到的所有内部链接的列表
def getInternalLinks(bsObj, includeUrl):
    print('bsObj:', bsObj)
    print('includeUrl:', includeUrl)

    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.findAll(
            "a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 检索在页面上找到的所有外部链接的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 查找以“http”或“www”开头的所有链接
    # 不包含当前URL
    for link in bsObj.findAll(
            "a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:  # 避免数组重复
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


# 获取随机外部链接
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)  # 打开最开始的连接
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(
            0,
            len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("随机外部链接是: " + externalLink)
    followExternalOnly(externalLink)


# 只遵循外部
followExternalOnly("http://oreilly.com")
