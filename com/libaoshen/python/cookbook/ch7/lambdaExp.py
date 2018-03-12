# coding:utf-8

"""
    lambda表达式
"""

# 其中的x是随着代码动态读取的
x = 10
f = lambda y: x + y
x = 20
print(f(10))

# 如果不想动态变化
f = lambda y, x=x: x + y
x = 30
print(f(20))