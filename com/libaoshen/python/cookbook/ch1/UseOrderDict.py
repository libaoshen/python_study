# coding:utf-8

# 使用OrderDict 实现有序字典, 因为字典是默认无序的

from collections import OrderedDict
import json

d = OrderedDict()

d['b'] = 1
d['a'] = 2
d['c'] = 3

print(d)
# 序列化为json字符串
print(json.dumps(d))