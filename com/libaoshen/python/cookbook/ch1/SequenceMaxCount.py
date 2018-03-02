# coding:utf-8

# 求序列中出现次数最多的元素

# 使用 Counter

from collections import Counter
import heapq

lst = [1, 2, 3, 4, 5, 1, 2, 4, 6, 2, 4, 7, 1, 9, 0, 8, 1, 0, 9]

word_count = Counter(lst)
common3 = word_count.most_common(3)
print(common3)

# 使用dic实现


def most_common(lst, n):
    dt = {}
    result = []

    for i in lst:
        if dt.get(i) is not None:
            dt[i] += 1
        else:
            dt[i] = 1

    lst2 = heapq.nlargest(len(dt), dt, key=lambda x: dt[x])

    for key in lst2:
        tp = list()
        tp.append(key)
        tp.append(dt[key])
        result.append(tuple(tp))

    return result[:n]


print(most_common(lst, 3))