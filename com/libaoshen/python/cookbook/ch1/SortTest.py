# coding:utf-8

# 序列排序

# sorted(obj, key)
from operator import itemgetter
from operator import attrgetter

priceInfo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'APPLE', 'shares': 50, 'price': 591.1},
    {'name': 'FB', 'shares': 200, 'price': 21.9},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.64}
]

# 使用lambda
print(sorted(priceInfo, reverse=True, key=lambda x: x['price']))
# 使用itemgetter
print(sorted(priceInfo, reverse=True, key=itemgetter('price')))

# 对象排序


class User:
    def __init__(self, userId):
        self.userId = userId

    def __repr__(self):
        return 'User{}'.format(self.userId)

# 使用对象的属性排序


users = [User(1), User(40), User(20)]
print(sorted(users, reverse=True, key=attrgetter('userId')))
