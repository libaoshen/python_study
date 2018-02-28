# coding:utf-8

# 使用heapq 实现优先级队列

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue =[]
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


pq = PriorityQueue()
pq.push('libaoshen', 10)
pq.push('wangzhi', 2)
pq.push('zhangtianyu', 3)
pq.push('yaohaoyu', 12)

print(pq.pop())
