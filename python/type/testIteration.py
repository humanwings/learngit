from collections.abc import Iterable 
from collections.abc import Iterator

ra = "AaBbCcDd"                 # string

lb = ["AAA","BBB","CCC"]        # list

tc = ("aaa","bbb","ccc")        # tuple

dd = {"QQQ":1,"WWW":2,"EEE":3}  # dict

se = {"RRR","TTT","YYY"}        # set

zh = zip(ra,lb)

ri = reversed(lb)

print("↓↓↓↓↓↓↓↓↓↓    is Iterable    ↓↓↓↓↓↓↓↓↓↓↓")

print(isinstance(ra,Iterable))
print(isinstance(lb,Iterable))
print(isinstance(tc,Iterable))
print(isinstance(dd,Iterable))
print(isinstance(se,Iterable))

print("↓↓↓↓↓↓↓↓↓↓    is Ierator     ↓↓↓↓↓↓↓↓↓↓↓")

print(isinstance(ra,Iterator))
print(isinstance(lb,Iterator))
print(isinstance(tc,Iterator))
print(isinstance(dd,Iterator))
print(isinstance(se,Iterator))
print(isinstance(zh,Iterator))
print(isinstance(ri,Iterator))

print("↓↓↓↓↓↓↓↓↓↓    copy test     ↓↓↓↓↓↓↓↓↓↓↓")

lb_2 = lb[:]
lb_3 = list(lb)
lb_2.append("DDD")
lb_3.append("EEE")
print(lb,lb_2,lb_3)
lb_2[0] = "FFF"
lb_3[0] = "GGG"
print(lb,lb_2,lb_3)
