'''
    yield from 结构最简单的用法
        委派生成器相当于管道，所以可以把任意数量的委派生成器连接在一起---
        一个委派生成器使用yield from 调用一个子生成器，而那个子生成器本身也是委派生成器，使用yield from调用另一个生成器。
        最终以一个只是用yield表达式的生成器（或者任意可迭代对象）结束。
'''

#! -*- coding: utf-8 -*-

from collections import namedtuple

Result = namedtuple('Result', 'count average')

# 子生成器
def averager():
    print("averager begin ")
    total = 0.0
    count = 0
    average = None
    while True:
        # main 函数发送数据到这里
        print("begin yield ...")
        term = yield
        print("term is ", term)
        if term is None: # 终止条件
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average) # 返回的Result 会成为grouper函数中yield from表达式的值


# 委派生成器
def grouper(results, key):
    print("grouper begin ")
     # 这个循环每次都会新建一个averager 实例，每个实例都是作为协程使用的生成器对象
    n = 0
    # 如果不用while，那么grouper结束时会发生StopIteration，导致程序中止
    # 有while在，grouper就不会结束，也就不会抛出StopIteration
    while True:
    # grouper 发送的每个值都会经由yield from 处理，通过管道传给averager 实例。grouper会在yield from表达式处暂停，等待averager实例处理客户端发来的值。
    # averager实例运行完毕后，返回的值绑定到results[key] 上。
        n += 1
        print("before yield from ", n)
        results[key] = yield from averager()
        print("after yield from ", n)


# 调用方
def main(data):
    results = {}
    for key, values in data.items():
        # group 是调用grouper函数得到的生成器对象，传给grouper 函数的第一个参数是results，用于收集结果；第二个是某个键
        print("------------ ", key, values)
        group = grouper(results, key)
        print("grouper OK")
        next(group)
        print("next OK")
        for value in values:
            # 把各个value传给grouper 传入的值最终到达averager函数中；
            # grouper并不知道传入的是什么，同时grouper实例在yield from处暂停
            group.send(value)
        # 把None传入grouper，传入的值最终到达averager函数中，导致当前实例终止。然后继续创建下一个实例。
        # 如果没有group.send(None)，那么averager子生成器永远不会终止，委派生成器也永远不会在此激活，也就不会为result[key]赋值
        group.send(None) # <-  send(None) 以后， main已经处理完当前数据，结束本次循环了，但是旧的group还在生成新的averager，等待数据。
    report(results)


# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':[40, 41, 42, 43, 44, 54],
    'girls;m': [1.5, 1.6, 1.8, 1.5, 1.45, 1.6],
    'boys;kg':[50, 51, 62, 53, 54, 54],
    'boys;m': [1.6, 1.8, 1.8, 1.7, 1.55, 1.6],
}

if __name__ == '__main__':
    main(data)