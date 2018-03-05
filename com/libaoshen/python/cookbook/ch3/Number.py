# coding:utf-8

"""
    数字
"""

from decimal import Decimal

# 1.数据四舍五入
a = 1.235
# 两个参数：第一个是目标数字，第二是舍入小数点后几位
b = round(a, 2)
print(b)

# 中间的数字，round会取得最近的偶数
a = 2.5
b = round(a)
print(b)

# 整数也可以舍入
a = 12346
b = round(a, -1)
print(b)

# 2.数字格式化
a = 1.2346
# x.yf : x是整体的站位长度，y是小数点后保留位数(会四舍五入)
b = format(a, "5.3f")
print(b)

# 2.浮点数的运算
a = 2
b = 3.2
c = a + b
d = b - a
# 注意到c的值为5.300000000000001,会出现一定的误差,因为python使用IEEE 754 标准存储浮点数
print(c)
print(d)
print((a + b) == 5.3)

# 如果想精确的计算，使用Decimal
a = Decimal('3.2')
b = Decimal('2.1')
c = a + b
print(c)
print(c == Decimal('5.3'))