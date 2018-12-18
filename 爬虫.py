import urllib.request

#最简单的爬虫(爬取百度首页数据)：
response = urllib.request.urlopen("https://www.baidu.com/").read()

print(response)