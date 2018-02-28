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