# coding:utf-8

"""
    迭代器实现node的深度优先
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.chirdren = []

    def __repr__(self):
        return "Node(value={})".format(self.data)

    def __iter__(self):
        return iter(self.chirdren)

    def addChirdren(self, node):
        self.chirdren.append(node)

    def depthFirst(self):
        yield self
        for c in self:
            yield from c.depthFirst()

if __name__ == '__main__':
    root = Node(0)
    chird1 = Node(1)
    chird2 = Node(2)
    root.addChirdren(chird1)
    root.addChirdren(chird2)
    chird1.addChirdren(Node(3))
    chird1.addChirdren(Node(4))
    chird2.addChirdren(Node(5))
    chird2.addChirdren(Node(6))

    for c in root.depthFirst():
        print(c)

