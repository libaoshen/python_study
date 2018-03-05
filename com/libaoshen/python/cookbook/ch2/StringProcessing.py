# coding:utf-8

'''
    python 英文字符串处理
'''
import re

str = "Python is a static type language"


# 一. 字符串基本操作


# a.获取字符串长度
length = len(str)
print("'", str, "' 的长度 = ", length)

# b.字符串索引
firstChar = str[0]
print("'", str, "' 第一个字符 = ", firstChar)

# c.字符串分片
# 1. 直接使用[a:b]
stringSlice = str[0:6]
print("'", str, "' [0:6] = ", stringSlice)
# 2. 定义分片对象
sli = slice(0, 6)
print("'", str, "' [0:6] = ", str[sli])

# d.字符串加法
newStr = str + str
print("'", str, "' + '" + str + "' = ", newStr)

# e.字符串乘法
newStr = str * 3
print("'", str, "' * 3 = ", newStr)

# f.判断成员资格
isExist = 'Python' in str
print("'", str, "' contain 'Python' = ", isExist)

# g.大小写转换
# 1.全体字母大小写转换
upper = str.upper()
lower = str.lower()
print("'", str, "' 大写形式 = ", upper)
print("'", str, "' 小写形式 = ", lower)
# 2.字符串首字母大写
capital = str.capitalize()
print("'", str, "' 首字母大写形式 = ", capital)
# 3.字符串中每个单词的首字母大写
title = str.title()
print("'", str, "' 每个单词首字母大写形式 = ", title)

# h.字符串检索
# 1.使用find
ind = str.find('Python')
print("'Python' 在 '", str, "' 中第一次出现的下标 = ", ind)
# 2.使用index
ind = str.index('Python')
print("'Python' 在 '", str, "' 中第一次出现的下标 = ", ind)

# i.字符串的分割
# 1.一个分割符
spl = str.split(" ")
print("'", str, "' 按照空格分隔后 = ", spl)
# 2.多个分割符(使用re模块中的split)
str2 = "Python;is a static,type language"
spl2 = re.split(r"[,\s;]", str2)
print("'", str, "' 按照空格、逗号、分号分隔后 = ", spl2)

# j.字符串的连接(和split互为逆操作)
joi = ",".join(spl)
print(spl, " 按照空格连接 = ", joi)

# k.字符串的替换
rep = str.replace("s", "S")
print("'", str, "' 中的s被S替换后 = ", rep)

# l.统计字符串中某个字符或字符串出现的次数
cnt = str.count("s")
print("'", str, "' 中的s出现次数 = ", cnt)

# m.去除字符串中首尾出现的字符
# 1.去除首尾空白(还有lstrip()和rstrip()分别去除左侧或右侧空白)
strp = " HelloWorld ".strip()
print("'   HelloWorld     ' 去除两侧空格后 = '", strp, "'")
# 2.去除首尾给定的字符
strp2 = "@@@HelloWorld!!!".strip('@!')
print("'@@@HelloWorld!!!' 去除两侧的'@'和'!'后 = '", strp2, "'")

# n.字符串中的判断方法
# 1.判断是否是数字
isNum = "1".isdigit()
print("'1' 是否是数字 = ", isNum)
# 2.判断是否是字母
isAlp = "Hello1".isalpha()
print("'Hello1' 是否是字母", isAlp)
# 3.判断是否是大小写
isUp = "HELLO".isupper()
print("'HelloWorld' 是否是大写 = ", isUp)
isLow = "hello".islower()
print("'hello' 是否是小写 = ", isLow)
# 4.判断字符串是否以某些字符串开头
# a. 判断一个字符或字符串
isStartWith = "HelloWorld".startswith("He")
print("'HelloWorld' 是否以 'He' 开头 = ", isStartWith)
# b. 判断多个字符或字符串
isStartWith = "HelloWorld".startswith(("He", "H", "e"))
print("'HelloWorld' 是否以 'He' 或 'H' 或 'e' 开头 = ", isStartWith)
# 5.判断字符串是否以某些字符串结束
isEndWith = "HelloWorld".endswith("ld")
print("'HelloWorld' 是否以 'ld' 结束 = ", isEndWith)


# 二. 使用re模块完成字符串的高级处理
# a.复杂字符串搜索匹配
# 简单匹配 match 时间 2017-12-11 格式的数据
str3 = "Yesterday is 2017-01-22.Today is 2017-01-23"
isMatch = re.match(r'.*?\d{4}-\d{2}-\d{2}.*?', str3)
print("'" + str3 + "' 是否匹配 '2017-12-11' 格式的数据 = ", isMatch)
# 使用pattern对象记录正则
pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
isMatch = pattern.match(str3)
print("'" + str3 + "' 是否匹配 '2017-12-11' 格式的数据 = ", isMatch)
# 查找匹配正则的数据 findall
matchData = pattern.findall(str3)
print("'" + str3 + "' 匹配 '2017-12-11' 格式的数据 = ", matchData)
# 使用group捕获分组
pattern = re.compile(r'.*?(\d{4})-(\d{2})-(\d{2}).*?')
matchData = pattern.match(str3)
groupData = matchData.groups()
year, month, day = groupData
print("'" + str3 + "' group '2017-12-11' 格式的数据 = ", groupData)
print("year = ", year, ",month = ", month, ", day = ", day)
matchData = pattern.findall(str3)
print("'" + str3 + "' group '2017-12-11' 格式的数据 = ", matchData)

# b.复杂字符串的替换
# 基本替换
newStr = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', str3)
print("'" + str3 + "' 中 '2017-12-11' 格式的数据转换为 '12/11/2017' 格式 = ", newStr)
# 忽略大小替换
newStr = re.sub('today', 'now', str3, flags=re.IGNORECASE)
print("'" + str3 + "' 'today' 忽略大小写 替换为 'now' = ", newStr)