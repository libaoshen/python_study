# coding:utf-8

"""
    查找词干
"""

import re


# 使用基本的循环判断
def stem(word):
    for suffix in ['ed', 'ly', 'ing']:
        if word.endswith(suffix):
            return word[:-len(suffix)]


# 使用正则
def stemInRe(word):
    return re.findall("^(.*)(?:ed|ly|ing)$", word)

print(stem('interesting'))
print(stemInRe('interesting'))