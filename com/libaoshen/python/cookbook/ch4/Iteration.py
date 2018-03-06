# coding:utf-8

"""
    迭代器
"""

# 1.遍历可迭代对象
a = [1, 2, 3, 4, 5]
b = iter(a)

print(next(b))

# 2.生成器
def generatrNum(start, end, incresement):
    a = start
    while a < end:
        yield a
        a += incresement

a = generatrNum(1, 10, 2)
print(next(a))
print(next(a))
print(next(a))