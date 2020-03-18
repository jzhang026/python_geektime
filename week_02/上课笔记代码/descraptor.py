# def property(fn):
#     # logic
#     def inner(*args, **kwarag):
#         # logic
#         return fn(*args, **kwargs)
#     return inner

class Human(object):
    def __init__(self, name):
        self.name = name

    # 将方法封装成属性
    # @property
    def gender(self):
        return 'M'

h1 = Human('Adam')

h2 = type(h1)('ada')