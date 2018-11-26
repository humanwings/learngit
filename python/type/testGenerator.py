import collections

# 只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g)
for n in g:
    # print(n)
    pass

print(isinstance(g, collections.Generator))
print(isinstance(g, collections.Iterable))
print(isinstance(g, collections.Iterator))

print()
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
import inspect

def fibg(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fibg(4)   # fibg此时并不开始执行，直到被调用next或者send函数

print(inspect.getgeneratorstate(g))
next(g)
print(inspect.getgeneratorstate(g))
g.close()
print(inspect.getgeneratorstate(g))
print("GEN_RUNNING # 解释器正在执行（只有在多线程应用中才能看到这个状态,本程序无法体现）")

