from twitter import Twitter, OAuth

# pip install twitter   安装twitter
# 确保添加应用程序的访问令牌和消费者密钥
t = Twitter(
    auth=OAuth("Access Token", "Access Token Secret", "Consumer Key",
               "Consumer Secret"))
pythonTweets = t.search.tweets(q="#python")
print(pythonTweets)  # 报错:由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。 可能需要翻墙