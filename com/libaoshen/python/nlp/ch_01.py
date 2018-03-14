# coding:utf-8

"""
    词长分布
"""

text1 = ["ofo", "is", "a", "Beijing", "based", "bicycle", "sharing", "company", "founded", "in", "2014"]

lenFreq = [len(word) for word in text1]

print(sorted(lenFreq))