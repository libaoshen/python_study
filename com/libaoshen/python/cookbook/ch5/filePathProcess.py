# coding:utf-8

"""
    文件路径相关处理操作
"""

import os
import sys

root = r"F:\sync_resource\datafile\first.txt"
root2 = r"F:\sync_resource\datafile"

# 判断路径是否存在
isExists = os.path.exists(root)
print(isExists)
# 判断是否是一个文件
isFile = os.path.isfile(root)
print(isFile)
# 判断是否是一个文件夹或目录
isDir = os.path.isdir(root)
print(isDir)
# 判断是否是一个链接文件
isLink = os.path.islink(root)
print(isLink)
# 获取真正的路径path
realPath = os.path.realpath(root)
print(realPath)
# 根据路径path获取文件名
fileName = os.path.basename(root)
print(fileName)
# 根据路径path获取文件夹路径
dir = os.path.dirname(root)
print(dir)
# 获取文件扩展名
splitText = os.path.splitext(root)
print(splitText)
# 根据系统的文件分隔符连接path
joinText = os.path.join("home", "webuser", "apache-tomcat", "bin", "start.sh")
print(joinText)
# 获取文件大小
fileSize = os.path.getsize(root)
print(fileSize)
os.path.getctime(root)
# 获取某个目录下的文件列表
fileList = [name for name in os.listdir(root2)]
print(fileList)
# 获取系统编码
print(sys.getdefaultencoding())