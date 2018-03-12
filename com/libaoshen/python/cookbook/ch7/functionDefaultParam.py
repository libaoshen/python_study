# coding:utf-8

"""
    函数默认参数
"""


def add(a, b, d = []):
    a + b
    return d


result = add(1, 2)
print(result)

result.append(1)
result.append(2)

result = add(3, 4)
print(result)