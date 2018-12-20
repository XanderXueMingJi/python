import os  # 提供了非常丰富的方法用来处理文件和目录
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"  # 图片下载存放的文件夹
baseUrl = "http://pythonscraping.com"  # 目标网站的地址


# 获取绝对URL
def getAbsoluteURL(baseUrl, source):
    # startswith 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
    # 如果参数 beg 和 end 指定值，则在指定范围内检查。
    if source.startswith("http://www."):  
        url = "http://" + source[11:]  # 只要第11个字符串后的字符
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url or ".js" in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):

    # http://pythonscraping.com/sites/default/files/lrg_0.jpg
    print('000000 absoluteUrl:', absoluteUrl)

    path = absoluteUrl.replace("www.", "")
    # http://pythonscraping.com/sites/default/files/lrg_0.jpg
    print('001 path:', path) 

    path = path.replace(baseUrl, "")
    print('002 path:', path)  # /sites/default/files/lrg_0.jpg

    path = downloadDirectory + path
    print('003 path:', path)  # downloaded/sites/default/files/lrg_0.jpg

    # os.path.dirname 去掉文件名，返回目录 
    directory = os.path.dirname(path)
    print('directory:', directory)  # downloaded/sites/default/files

    if not os.path.exists(directory):
        os.makedirs(directory)  # os.makedirs()创建多层目录

    # downloaded/sites/default/files/lrg_0.jpg
    print('after path:', path)
    return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)  # 只要有src属性的标签都会放入数组内

print('downloadList:', downloadList)

for download in downloadList:
    print('download["src"]:', download["src"])  # 将src从数组标签内提取出来
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        # urlretrieve 直接将远程数据下载到本地。
        urlretrieve(fileUrl,
                    getDownloadPath(baseUrl, fileUrl, downloadDirectory))
