'''
装饰器， 不使用@符号。
使用@的版本，请参照testDecorator_With@.py
'''

# ======================     无参数的装饰器 =====================
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def now11():
    print('2015-3-25')

now11 = log(now11)
now11()
print()

# ======================     有参数的装饰器   =========================

def logging(level): 
    def log(func): 
        def wrapper(*args, **kw):  
            print('call %s %s():' % (level,func.__name__)) 
            return func(*args, **kw) 
        return wrapper 
    return log 

def now2():
    print('2017-11-13') 

log = logging(level="warning")
now2 = log(now2)
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

def now3():
    print('2017-11-14')

now3 = w2(now3)
now3 = w1(now3)
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



def now4():
    print('2017-11-14')

now4 = Foo(now4)
now4()

