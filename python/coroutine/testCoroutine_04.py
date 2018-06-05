'''
    获取generator的返回值
'''

print("----------------  获取generator的返回值  ------------------")
from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break  # 为了返回值，协程必须正常终止；这里是退出条件
        total += term
        count += 1
        average = total/count
    # 返回一个namedtuple，包含count和average两个字段。在python3.3前，如果生成器返回值，会报错
    return Result(count, average)   # 返回值作为StopIteration异常的value

coro_avg = averager()
next(coro_avg)
coro_avg.send(20) # 并没有返回值
coro_avg.send(30)
coro_avg.send(40)
try:
    coro_avg.send(None)
except StopIteration as exc:
    print(exc.value)

