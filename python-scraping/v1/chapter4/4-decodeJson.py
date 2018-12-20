import json
from urllib.request import urlopen


# 运行失败
def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" +
                       ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")


print(getCountry("50.78.253.58"))