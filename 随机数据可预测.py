import datetime
import random

print('datetime.datetime.now():', datetime.datetime.now())
print('random.seed(datetime.datetime.now()):', random.seed(datetime.datetime.now()))


pages = set()
sstr = 'http://www.pythonscraping.com/misc/jquery.js?v=1.4.4'
print('pages:', pages)
print('sstr[11:]:', sstr[11:])