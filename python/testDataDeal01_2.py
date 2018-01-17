import os
import sys
import mycommon

jamesfile = "D:\doc\python\HeadFirstPythonFiles\james.txt"
juliefile = "D:\doc\python\HeadFirstPythonFiles\julie.txt"
mikeyfile = "D:\doc\python\HeadFirstPythonFiles\mikey.txt"
sarahfile = "D:\doc\python\HeadFirstPythonFiles\sarah.txt"

ja = mycommon.Runner(jamesfile)
print(ja.name,"(",ja.years,")'s top 3 speeds are ",ja.getTop3())

ju = mycommon.Runner(juliefile)
print(ju.name,"(",ju.years,")'s top 3 speeds are ",ju.getTop3())

mi = mycommon.Runner(mikeyfile)
print(mi.name,"(",mi.years,")'s top 3 speeds are ",mi.getTop3())

sa = mycommon.Runner(sarahfile)
print(sa.name,"(",sa.years,")'s top 3 speeds are ",sa.getTop3())
