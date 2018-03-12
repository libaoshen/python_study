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

# 3.奇数数列生成器
def oddGenerator(n):
    a = 1
    count = 1
    while count <= n:
        yield a
        a += 2
        count+=1

b = oddGenerator(10)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

# 循环使用
for n in oddGenerator(10):
    print(n)