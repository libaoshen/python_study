# coding:utf-8

# 各种推导表达式

# 列表推导表达式
lst = [i if i > 5 else -1 for i in range(10)]
print(lst)

# 生成器推导表达式
gene = (i for i in range(10))
print(gene)
for i in gene:
    print(i)

# 字典推导表达式
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
dct = {key: value for key, value in prices.items() if value > 10 }
print(dct)

# 过滤器


def isInt(val):
    try:
        i = int(val)
        return True
    except ValueError:
        return False


lst2 = ['a', 1, 's', '4', '2', '3', 8]
print(list(filter(isInt, lst2)))
