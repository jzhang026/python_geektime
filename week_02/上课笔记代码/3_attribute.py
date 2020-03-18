class Human(object):
    def __init__(self, name):
        self.name = name

    # def __getattr__(self, item):
    #     print('Human:__getattr__')
    #     self.item = item
    #     if self.item == 'fly':
    #         return 'superman'
    # def __getattribute__(self, item):
    #     print('human: __getattribute__')
    # def __getattribute__(self, name):
    #     print('arritbute %s' % (name,))
    def __getattr__(self, name):
        print('attr %s' % (name,)) 

h1 = Human('a')
print(h1.__dict__)
print(h1.sss)
print(h1.name)