# coding : utf-8

# 解析

# 1. 基本解析
# 普通序列
lst1 = ['a', 'b', 'c']
a, b, c = lst1

print(a, b, c)

# 字符串
str1 = "hello"
a, b, c, d, e = str1
print(a, b, c, d, e)

# 元祖
tuple1 = ('a', 'b', 'c')
a, b, c = tuple1
print(a, b, c)

# 混合
lst2 = ['a', 'b', ('1', '2')]
a, b, c = lst2
print(a, b, c)
a, b, (c, d) = lst2
print(a, b, c, d)


# 使用 * 解析
*a, b, c = [1, 2, 3, 4]
print(a, b, c)
a, b, *c = [1, 2, 3, 4, 5]
print(a, b, *c)

# 应用1：使用unpack功能实现复杂序列的循环
lst3 = [
    ("first", 1, 4),
    ("second", "hello")
]


def Sum(a, b):
    return a + b


def prit(s):
    print(s)


for key, *args in lst3:
    if key == "first":
        print(Sum(*args))
    if key == "second":
        prit(*args)