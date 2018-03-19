# coding:utf-8

"""
    类的模板
"""


class ClassTemplate:
    def __init__(self, x, y):
        """
        默认对象初始化函数
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        默认的对象字符串函数
        :return:
        """
        return "Point(%(x)s, %(y)s)" % {"x": self.x, "y": self.y}

    def __repr__(self):
        """
         默认的对象字符串函数，一般用在交互式环境中
         :return:
        """
        return "Point(%(x)s, %(y)s)" % {"x": self.x, "y": self.y}


first = ClassTemplate(1, 2)
print(first)