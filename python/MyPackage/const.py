# -*- coding: utf-8 -*-

# 定义常量
class _const:
    class ConstError(TypeError) :       # 声明一个异常类，用于在常量被修改或者删除时抛出
        pass
    
    def __init__(self):
        self.MYAGE = 40
        self.MYCOMPANY = "南京聯迪信息系統股份有限公司"

    def __setattr__(self, key, value):  # 通过对object.__setattr__()的重写，来保证常量只能新规，不能变更。
        if key in self.__dict__ :
            raise self.ConstError("不能变更常量的值："+ key)
        self.__dict__[key] = value
    
    def __delattr__(self, key):  # 通过对object.__delattr__()的重写，来保证常量只能新规，不能删除。
        if key in self.__dict__ :
            raise self.ConstError("不能删除常量的值："+ key)
        raise NameError("不存在的变量："+ key)

import sys

sys.modules[__name__] = _const()