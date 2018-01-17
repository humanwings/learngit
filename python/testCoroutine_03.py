"""
协程(Coroutine)测试  -  模拟:grep -rl 'root' /etc
"""

import os
def deco(func):  # 用来开启协程
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        print(args,kwargs)
        next(res)  # res.send(None)
        return res
    return wrapper

@deco
def search(target):  #  获取一个文件的绝对路径，并将這个绝对路径通过send()方法，在传递给下个含有yield的函数，也就是下面的opener函数。
    while True:
        PATH = yield
        g = os.walk(PATH)  # 获取PATH目录下的文件，文件夹
        for par_dir, dirs, files in g:  #迭代解包,取出当前目录路径和文件名
            print(par_dir)
            for file in files:
                file_path = r'%s\%s' %(par_dir,file)  # 拼接文件的绝对路径
                if (os.path.splitext(file_path)[1]) == ".txt":
                    target.send(file_path)  # 给下一个

@deco
def opener(target, pattern=None):  #  
    while True:
        file_path = yield
        with open(file_path, encoding='Shift_JIS') as f:
            target.send((file_path, f))  # 将文件路径和文件对象一起传递给下一个函数的yield，因为在打印路径时候，需要打印出文件路径，只有从这里传递下去

@deco
def cat(target):
    while True:
        filepath, f = yield # 这里接收opener传递进来的路径和文件对象
        for line in f:
            tag = target.send((filepath, line))  # 同样，也要传递文件路径,并且获取下一个函数grep的返回值，从而判断该文件是否重复读取了
            if tag:  # 如果为真，说明该文件读取过了，则执行退出循环
                break

@deco
def grep(target, pattern):
    tag = False
    while True:
        filepath, line = yield tag  # 接受两个值，并且设置返回值，這个返回值要传递给发送消息的send()，也就是cat()函数send
        tag = False
        if pattern in line:  # 如果待匹配字符串在该行
            target.send(filepath)   # 把文件路径传递给printer
            tag = True   # 设置tag

@deco
def printer():
    while True:
        filename = yield
        print(filename)

PATH1 = r'D:\work\99.tmp'
search(opener(cat(grep(printer(), 'root')))).send(PATH1)