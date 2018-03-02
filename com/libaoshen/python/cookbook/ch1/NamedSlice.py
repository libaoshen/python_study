# coding:utf-8

# 命名切片
# 为什么要命名切片？减少硬编码

lst = [1, 2, 3, 4, 5]

a = lst[2:4]
print(a)

# 使用slice定义切片
sl = slice(2, 4, 1)

b = lst[sl]
print(b)

# 切片使用
start = sl.start
end = sl.stop
step = sl.step

print(start, step, end)

# indices
st = "HelloWorld"
print(sl.indices(len(st)))
