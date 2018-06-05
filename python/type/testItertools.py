import itertools, collections

naturals = itertools.count(3, step = 4)  #  返回无限数列的iterator
print(isinstance(naturals, collections.Iterator))

cycle = itertools.cycle("1589")  #  返回指定序列的无限循环的iterator
print(isinstance(cycle, collections.Iterator))

rep = itertools.repeat("ABC", 10)  #  返回指定元素的指定次数的iterator
print(isinstance(rep, collections.Iterator))

ns = itertools.takewhile(lambda x: x <= 10, naturals) #  按照指定的过滤函数来过滤iterator
print(isinstance(ns, collections.Iterator))

