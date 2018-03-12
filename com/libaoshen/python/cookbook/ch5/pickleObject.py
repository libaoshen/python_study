# coding:utf-8

"""
    序列化对象
"""

import pickle

root = r"F:\sync_resource\datafile\third.txt"
# 序列化
data = [1, 2, 3, 4]
f = open(root, "wb")
pickle.dump(data, f)

# 反序列化
f = open(root, "rb")
data = pickle.load(f)
print(data)