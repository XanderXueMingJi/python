from twitter import Twitter, OAuth

# 确保添加应用程序的访问令牌和消费者密钥
t = Twitter(
    auth=OAuth("Access Token", "Access Token Secret", "Consumer Key",
               "Consumer Secret"))
statusUpdate = t.statuses.update(status='Hello, world!')
print(statusUpdate)