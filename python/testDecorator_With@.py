'''
装饰器， 使用@符号。
不使用@的版本，请参照testDecorator_No@.py
'''

# ======================     无参数的装饰器 =====================
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now11():
    print('2015-3-25')

now11()
print()

# ======================     有参数的装饰器   =========================

def logging(level):             # 2
    def log(func):             # 4
        def wrapper(*args, **kw):                # 6
            print('call %s %s():' % (level,func.__name__))             # 9
            return func(*args, **kw)             # 10
        return wrapper             #7
    return log             # 5

@logging(level="warning")
def now2():
    print('2017-11-13')             # 11

now2()
print()

# ======================     多个的装饰器   =========================

def w1(func): 
    print("w1")
    def wrapper(*args, **kw): 
        print("before func w1")
        ret = func(*args, **kw)
        print("after func w1")
        return ret
    return wrapper

def w2(func): 
    print("w2")
    def wrapper(*args, **kw): 
        print("before func w2")
        ret = func(*args, **kw)
        print("after func w2")
        return ret
    return wrapper

@w1
@w2
def now3():
    print('2017-11-14')

now3()
print()

# ======================     类装饰器   =========================

class Foo(): 
    
    def __init__(self,func):
        self._func = func
    
    def __call__(self):
        print("class decorator running")
        self._func()
        print("class decorator ending")


@Foo
def now4():
    print('2017-11-14')

now4()