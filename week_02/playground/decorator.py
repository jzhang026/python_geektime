import functools
def dec(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)
    return inner

@dec
def target(a):
    print('sfsdfsadfas: %s' % a)
    return a

@dec
def fn(b, c):
    print('this is bc: %s %s' % (b, c))
target('target a')
fn('aa', 'bb')


# template 装饰器模版
def dec(fn):
    # logic code ...
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        # logic code ....
        return fn(*args, **kwargs)
    return inner

        