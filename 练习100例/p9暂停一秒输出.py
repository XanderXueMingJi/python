# 暂停一秒输出

import time

obj = {
    'name': 'xmj',
    'age': 28,
    'love': 'book'
}

print(obj)

for key in obj:
    time.sleep(1)
    print('key:', key, 'val:', obj[key])
    