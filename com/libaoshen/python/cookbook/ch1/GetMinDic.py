# coding:utf-8

# 获取字典中的最大或最小值

d = {
    "a": 42.5,
    "b": 22,
    "c": 30,
    "d": 50,
    "e": 3
}

# 1. 使用zip
min1 = min(zip(d.values(), d.keys()))
max1 = max(zip(d.values(), d.keys()))

print(max1, min1)

# 2. 使用key
min2 = min(d, key=lambda k: d[k])
max2 = max(d, key=lambda k: d[k])

print(max2, ':', d[max2], ',', min2, ':', d[min2])