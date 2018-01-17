'''
    yield from : 
        在生成器 gen 中使用 yield from subgen()时，subgen 会获得控制权，把产出的值传个gen的调用方，即调用方可以直接控制subgen。于此同时，gen会阻塞，等待subgen终止。
        对于yield from 结构来说，解释器不仅会捕获StopIteration异常，还会把value属性的值变成yield from 表达式的值
        主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，使两者可以直接发送和产出值，还可以直接传入异常，而不用在中间的协程添加异常处理的代码。
'''

print("\n----------------  yield from 递归 ------------------")
# Example of flattening a nested sequence using subgenerators

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x) # 这里递归调用，如果x是可迭代对象，继续分解
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)


print("\n----------------  yield from 基本 ------------------")
'''
    A = yield  B        A是调用处send()的值， B是generator的yield语句返回值
    A = yield from B    B是子generator, A是B的return时StopIteration的value， 
'''

def outer():
    print("before outer 1")
    x = yield from middle() # yield from表达式的值是子生成器终止(return)时传给StopIteration异常的第一个参数(value), StopIteration不会继续向外抛
    print("before outer ", x)
    x = yield from middle() 
    print("after outer ", x)
    return "outer"      # 生成器退出时，生成器（或子生成器）中的return expr 表达式会触发 StopIteration(expr) 异常抛出。

def middle():
    print("before middle 1")
    x = yield from inner()  # yield from表达式的值是子生成器终止(return)时传给StopIteration异常的第一个参数(value), StopIteration不会继续向外抛
    print("before middle ", x)
    x = yield from inner()
    print("after middle ", x)
    return "middle"     # 生成器退出时，生成器（或子生成器）中的return expr 表达式会触发 StopIteration(expr) 异常抛出。

def inner():
    print("before inner 1")
    x = yield 3         # 子生成器产出的值都直接传给委派生成器的调用方（send函数）
    print("before inner ", x)
    x = yield 4         # 子生成器产出的值都直接传给委派生成器的调用方（send函数）
    print("after inner ", x)
    return "inner"      # 生成器退出时，生成器（或子生成器）中的return expr 表达式会触发 StopIteration(expr) 异常抛出。

g = outer()

print(next(g))

print(g.send(99))
print(g.send(99))
print(g.send(99))
print(g.send(99))
print(g.send(99))
print(g.send(99))
print(g.send(99))
print(g.send(None))
