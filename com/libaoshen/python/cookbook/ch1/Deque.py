# coding:utf-8

# deque 实现保存最后的N个元素

from collections import deque

# 1.deque的简单操作
dq = deque(maxlen=5)  # 队列最大容量为5
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)

print(dq)

dq.append(6)

print(dq)

# 出队列
d = dq.pop()
print(d)

# 应用1: 获取最后的N个元素
lst1 = [1, 2, 3, 4, 5]
dq2 = deque(maxlen=2)

for num in lst1:
    dq2.append(num)

print(dq2)



