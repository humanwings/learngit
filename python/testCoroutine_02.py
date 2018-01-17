'''
协程(Coroutine)测试   -   装饰器
'''
print("--------------------  添加数据  ---------------------")
def deco(func):
    def wrapper():
        res = func()
        next(res) 
        return res
    return wrapper

@deco
def foo():
    food_list = []
    while True:
        food = yield food_list  #返回添加food的列表
        food_list.append(food)
        print("elements in foodlist are:",food)
        
g = foo()
print(g.send('苹果'))
print(g.send('香蕉'))
print(g.send('菠萝'))


print("--------------------  throw和close  ---------------------")
import inspect

class DemoException(Exception):
    pass

def coroutinue(func):
    '''
    装饰器： 向前执行到第一个`yield`表达式，预激`func`
    :param func: func name
    :return: primer
    '''    
    def primer(*args, **kwargs):
        # 把装饰器生成器函数替换成这里的primer函数；调用primer函数时，返回预激后的生成器。
        gen = func(*args, **kwargs)        # 调用被被装饰函数，获取生成器对象
        next(gen)  # 预激生成器
        return gen  # 返回生成器
    return primer
    
@coroutinue
def exc_handling():
    print('-> coroutine started')    
    try:
        while True:        
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Conginuing...')
            else:            # 如果没有异常显示接收到的值
                print('--> coroutine received: {!r}'.format(x))    
    finally:
        print('-> coroutine ending')

exc_coro = exc_handling()

exc_coro.send(11)
exc_coro.send(12)
exc_coro.send(13)

exc_coro.throw(DemoException) # 向协程发送其可以处理的异常，协程不会中止；但是如果传入的是未处理的异常，协程会终止
print(inspect.getgeneratorstate(exc_coro))

exc_coro.close()
print(inspect.getgeneratorstate(exc_coro))

