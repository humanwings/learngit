# memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片。
# 它让你在不需要复制内容的前提下，在数据结构之间共享内存。其中数据结构可以是任何形式，比如 PIL 图片、SQLite 数据库和 NumPy 的数组，等等。

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])

for x in numbers:
    print("{:x}".format(x))

memv = memoryview(numbers)

print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5]=4

print(numbers)