# coding:utf-8

"""
    函数元信息
"""


def add(a:int, b:int) -> int:
    return a + b

print(add(4, 2))
print(add.__annotations__)
help(add)