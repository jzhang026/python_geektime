class Human(object):
    live = True
    _age = 0
    __fly = 'adfa'
    def __init__(self, name):
        self.name = name
    def __getattr__(self, prop):
        print('not exist %s' % prop)
        return None
    def __getattribute__(self, props):
        print('also not exist %s' % props)
        try:
            return super().__getattribute__(props)
        except Exception as e:
            return None


man = Human('z')
woman = Human('k')
