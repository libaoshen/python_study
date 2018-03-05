# coding:utf-8

# 查找两个字典的相同点

a = {
    "a": '1',
    "b": '2',
    "c": '3'
}

b = {
    "a": '4',
    "e": '5',
    "f": '6'
}

print(a.keys() & b.keys())
print(type(a.values()))