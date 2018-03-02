# coding:utf-8

# 一个键对应多个值 的映射: 一个键对应一个list或set

from collections import defaultdict

# 1. 使用defaultdic, dict的子类, 创建具有初始值的dict
d = defaultdict(list) # list有序

print(isinstance(d, dict))

d['a'].append('a')
d['b'].append('c')
d['a'].append(1)

print(d)

d2 = defaultdict(set) # set无序

d2['a'].add('a')
d2['b'].add(1)
d2['a'].add(2)

print(d2)

# 2. 直接使用原始的dict,使用setdefault, 为键设置默认值
d3 = {}

d3.setdefault('a', []).append(1)
d3.setdefault('b', []).append(2)
d3.setdefault('a', []).append('a')

print(d3)
