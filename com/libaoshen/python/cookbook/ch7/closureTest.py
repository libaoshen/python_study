# coding:utf-8

"""
    闭包: 闭包就是函数里面再定义函数，我们称第一个函数为外函数，第二个函数为内函数。同时，内函数使用外函数定义的变量
    外函数结束时返回内函数引用，这就形成了一个闭包
    用途：主要用在装饰器；
"""


def outer(a):
    def inner(b):
        nonlocal a
        a+=b
        return a + b

    return inner

f = outer(10)
print(f(10))
print(f(20))

