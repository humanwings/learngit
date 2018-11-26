
# 在python中实现了__iter__方法的对象是可迭代的，实现了next()方法的对象是迭代器
# 一个迭代器工作，至少要实现__iter__方法和next方法
class test():
    def __init__(self,data=1):
        self.data = data

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data+=1
            return self.data

for item in test(3):
    print(item)