'''
协程(Coroutine)测试   -   生产者和消费者模型
'''

def consumer():
    r = ''
    # print('*' * 10, '1', '*' * 10)
    while True:
        # print('*' * 10, '2', '*' * 10)
        n = yield r
        if not n:
            # print('*' * 10, '3', '*' * 10)
            return
        # print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    # print('*' * 10, '4', '*' * 10)
    c.send(None)      # 相当于 c.next()  不能send非none 因为是第一次调用，没有yield来接收数据
    n = 0
    # print('*' * 10, '5', '*' * 10)
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    #c.send(0)      # 在这里加上send(0)，可以出return前的log，但是会发生topIteration，为什么？
    c.close()

c = consumer()
produce(c)

