# coding:utf-8

"""
    json处理
"""

import json

dict1 = {"first": "li", "second": "baoshen"}
lst2 = [1, 2, 3, 4]

# python对象转换为json字符串
dictJsonString = json.dumps(dict1)
print(dictJsonString)
dictJsonString = json.dumps(lst2)
print(dictJsonString, type(dictJsonString))
# json字符串转换为python对象
jsonObject = json.loads(dictJsonString)
print(jsonObject, type(jsonObject))