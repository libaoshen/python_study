# coding:utf-8

# 序列groupby

from operator import itemgetter
from itertools import groupby

priceInfo = [{'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'APPLE', 'shares': 50, 'price': 591.1},
             {'name': 'FB', 'shares': 100, 'price': 21.9}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 50, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.64}]

# 排序
priceInfo.sort(key=itemgetter('shares'))
# groupBy

for shares, items in groupby(priceInfo, key=itemgetter('shares')):
    print(shares)
    for item in items:
        print(item)