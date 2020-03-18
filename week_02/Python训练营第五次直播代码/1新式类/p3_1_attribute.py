class Desc(object):
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        print(f'__get__{instance} {owner}')
        return self.name

    def __set__(self, instance, value):
        print(f'__set__{instance} {value}')
        self.name = value

    def __delete__(self, instance):
        print(f'__get__{instance}')
        del self.name

class MyObj(object):
    a = Desc('aaa')
    b = Desc('bbb')

myObj = MyObj()
myObj.a
myObj.a = 'ab'