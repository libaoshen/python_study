# coding:utf-8

# heapq 堆 实现获取最大或最小的N个元素

import heapq

# 1.基本操作
nums = [1, 2, 4, -2, 2, 9, 0, 12, 1, -5]
# 获取最大的N个元素
print(heapq.nlargest(3, nums))
# 获取最小的N个元素
print(heapq.nsmallest(3, nums))

# 2.作用于复杂的数据结构
priceInfo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'APPLE', 'shares': 50, 'price': 591.1},
    {'name': 'FB', 'shares': 200, 'price': 21.9},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.64}
]

cheap = heapq.nsmallest(3, priceInfo, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, priceInfo, lambda s: s['price'])
print(expensive)