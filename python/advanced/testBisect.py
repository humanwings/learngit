import bisect
import sys


# bisect 可以用于list 和 array.array
data = [43, 31,15,24,135,81,2,34,11, 103, 130,23]

data.sort()                                 # 使用这个模块的函数前先确保操作的列表是已排序的。
print(data)

print(bisect.bisect(data, 43))              #查找该数值将会插入的位置并返回(相等时返回前面的位置)，而不会插入。
print(bisect.bisect_left(data, 43))         #查找该数值将会插入的位置并返回(相等时返回后面的位置)，而不会插入。
print(bisect.bisect_right(data, 43))        #bisect_right = bisect

bisect.insort(data, 43)                     #查找该数值将会插入的位置并插入
bisect.insort_left(data, 43,1,3)            #查找该数值将会插入的位置并插入,比较对象是从[1]为止开始3-1=2个元素
bisect.insort_right(data, 43,12,14)

print(data)

print("--------------------------------------------------------")

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'
def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle) 
        # position = bisect_fn(HAYSTACK, needle, 4,6) 
        offset = position * '  |'    
        print(ROW_FMT.format(needle, position, offset)) 

if sys.argv[-1] == 'left': 
    bisect_fn = bisect.bisect_left  
else:
    bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__) 
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)

print("--------------------------------------------------------")