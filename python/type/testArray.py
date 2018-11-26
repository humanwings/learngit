import array
import random
import bisect

arr = array.array('i',(random.randint(1,100) for i in range(10)))
print(arr)
print(arr[-1])

# 数组排序
sortarr = array.array(arr.typecode, sorted(arr))
print(sortarr)

# 有序插入
bisect.insort(sortarr, 37)
print(sortarr)

