# coding:utf-8

"""
    文件demo
"""

import os

root = r"F:\sync_resource\datafile\\"

# 1.基本使用
# 读文件
# 将整个文件读取为一个字符串
with open(root + "first.txt", "rt") as f:
    print(f.read())

# 迭代读取文件
with open(root + "first.txt", "rt") as f:
   for line in f:
       print(line)

with open(root + "first.txt", "rt") as f:
   line = f.readline()
   while line != None and line != '\n' and line.strip() != '':
       print(line)
       line = f.readline()

# 写文件
with open(root + "first.txt", "at", encoding="gbk") as f:
    print(f.write("你好 谢谢你们"))

# 打印到文件
with open(root + "second.txt", "at", encoding="gbk") as f:
    print("你好，我叫lbs，我来自中国！Hello, my name is lbs and i come from China!", file=f)

# print 的高级使用
print("H", "U", "A", "W", "E", "I", sep=".", end="!")
lst = list("HUAWEI")
# 函数调用中使用*,表示将列表转换为参数列表
print(*lst, sep=".", end="!")

# 2.文件其他操作
# 判断文件是否存在
print(os.path.exists(root + "second.txt"))
print(os.path.exists(root + "third.txt"))