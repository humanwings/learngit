import bisect

data = [43, 31,15,24,135,81]

data.sort()                                 # 使用这个模块的函数前先确保操作的列表是已排序的。
print(data)

print(bisect.bisect(data, 43))              #查找该数值将会插入的位置并返回，而不会插入。
print(bisect.bisect_left(data, 43))
print(bisect.bisect_right(data, 43))

bisect.insort(data, 43)                     #查找该数值将会插入的位置并插入
bisect.insort_left(data, 43)
bisect.insort_right(data, 43)

print(data)